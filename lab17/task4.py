import csv
import re
import sys
from collections import Counter
from statistics import median
def remove_html_tags(text):
    return re.sub(r'<.*?>', '', text)
def standardize_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = remove_html_tags(text)
    return text.strip()
def tokenize(text):
    # Simple whitespace tokenizer
    return re.findall(r'\b\w+\b', text)
def compute_tfidf(corpus):
    # corpus: list of strings
    tokenized_corpus = [tokenize(doc) for doc in corpus]
    vocab = sorted(set(token for doc in tokenized_corpus for token in doc))
    vocab_index = {word: idx for idx, word in enumerate(vocab)}
    N = len(corpus)
    # Document frequency
    df = Counter()
    for doc in tokenized_corpus:
        for token in set(doc):
            df[token] += 1
    # Compute TF-IDF vectors
    tfidf_vectors = []
    for doc in tokenized_corpus:
        tf = Counter(doc)
        doc_len = len(doc) if len(doc) > 0 else 1
        vec = [0.0] * len(vocab)
        for token in tf:
            tf_val = tf[token] / doc_len
            idf_val = 0.0
            if df[token]:
                idf_val = (N / df[token])
            vec[vocab_index[token]] = tf_val * idf_val
        tfidf_vectors.append(vec)
    return tfidf_vectors, vocab
def read_reviews_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            review = row.get('review', '').strip()
            rating = row.get('rating', '').strip()
            # Standardize text
            review_clean = standardize_text(review)
            # Handle missing rating
            try:
                rating_val = float(rating)
            except (ValueError, TypeError):
                rating_val = None
            data.append({'review': review_clean, 'rating': rating_val})
    return data
def fill_missing_ratings(data):
    ratings = [row['rating'] for row in data if row['rating'] is not None]
    med = median(ratings) if ratings else 5.0
    for row in data:
        if row['rating'] is None:
            row['rating'] = med
    return data
def normalize_ratings(data):
    for row in data:
        # Assume ratings are 0-10, map to 0-1
        row['rating_normalized'] = float(row['rating']) / 10.0 if row['rating'] is not None else 0.5
    return data
def generate_summary_report(before_data, after_data):
    n_before = len(before_data)
    n_after = len(after_data)
    missing_before = sum(1 for row in before_data if row['rating'] is None)
    missing_after = sum(1 for row in after_data if row['rating'] is None)
    print("Summary Report:")
    print(f"Total reviews: {n_before}")
    print(f"Missing ratings before: {missing_before}")
    print(f"Missing ratings after: {missing_after}")
    print("Sample review before cleaning:")
    for row in before_data:
        if row['review']:
            print(" ", row['review'][:100])
            break
    print("Sample review after cleaning:")
    for row in after_data:
        if row['review']:
            print(" ", row['review'][:100])
            break
def write_cleaned_reviews(data, tfidf_vectors, vocab, output_file):
    # Write as CSV: review, rating, rating_normalized, tfidf_vector (as string)
    fieldnames = ['review', 'rating', 'rating_normalized'] + [f"tfidf_{w}" for w in vocab]
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row, vec in zip(data, tfidf_vectors):
            row_out = {
                'review': row['review'],
                'rating': row['rating'],
                'rating_normalized': row['rating_normalized'],
            }
            for i, w in enumerate(vocab):
                row_out[f"tfidf_{w}"] = vec[i]
            writer.writerow(row_out)
def main():
    filename = input("Enter reviews CSV filename: ")
    before_data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            review = row.get('review', '').strip()
            rating = row.get('rating', '').strip()
            try:
                rating_val = float(rating)
            except (ValueError, TypeError):
                rating_val = None
            before_data.append({'review': review, 'rating': rating_val})
    data = read_reviews_csv(filename)
    data = fill_missing_ratings(data)
    data = normalize_ratings(data)
    # Tokenize and encode using TF-IDF
    corpus = [row['review'] for row in data]
    tfidf_vectors, vocab = compute_tfidf(corpus)
    # Generate summary report
    generate_summary_report(before_data, data)
    # Write cleaned dataset
    output_file = 'cleaned_' + filename
    write_cleaned_reviews(data, tfidf_vectors, vocab, output_file)
    print(f"A cleaned dataset ready for sentiment classification.")
if __name__ == "__main__":
    main()
