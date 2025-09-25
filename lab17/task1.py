import csv
import string
# Define stopwords (a small sample, expand as needed)
STOPWORDS = set([
    'the', 'is', 'at', 'which', 'on', 'and', 'a', 'an', 'to', 'in', 'for', 'of', 'with', 'by', 'from', 'it', 'this', 'that'
])
def clean_text(text):
    # Remove punctuation and special symbols
    text = ''.join(ch for ch in text if ch.isalnum() or ch.isspace())
    # Remove stopwords
    words = text.lower().split()
    words = [w for w in words if w not in STOPWORDS]
    return ' '.join(words)
def parse_datetime(timestamp):
    # Expected format: 'YYYY-MM-DD HH:MM:SS'
    try:
        date_part, time_part = timestamp.strip().split(' ')
        year, month, day = map(int, date_part.split('-'))
        hour, minute, second = map(int, time_part.split(':'))
        # Calculate weekday (0=Monday, 6=Sunday) using Zeller's Congruence
        q = day
        m = month
        Y = year
        if m < 3:
            m += 12
            Y -= 1
        K = Y % 100
        J = Y // 100
        h = (q + 13*(m+1)//5 + K + K//4 + J//4 + 5*J) % 7
        weekday = (h + 6) % 7  # 0=Monday
        return hour, weekday
    except:
        return None, None
def is_spam(post_text):
    # Simple spam detection: repeated words or excessive length
    words = post_text.lower().split()
    if len(words) > 100:
        return True
    if len(set(words)) < len(words) // 2:
        return True
    return False
def read_and_clean_csv(filename):
    cleaned_data = []
    seen_posts = set()
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            post_text = row.get('post_text', '').strip()
            likes = row.get('likes', '').strip()
            shares = row.get('shares', '').strip()
            timestamp = row.get('timestamp', '').strip()
            # Handle missing values
            likes = int(likes) if likes.isdigit() else 0
            shares = int(shares) if shares.isdigit() else 0
            # Clean post text
            cleaned_post = clean_text(post_text)
            # Remove spam/duplicates
            post_key = cleaned_post
            if post_key in seen_posts or is_spam(cleaned_post):
                continue
            seen_posts.add(post_key)
            # Extract datetime features
            hour, weekday = parse_datetime(timestamp)
            cleaned_data.append({
                'post_text': cleaned_post,
                'likes': likes,
                'shares': shares,
                'hour': hour,
                'weekday': weekday
            })
    return cleaned_data
def main():
    filename = input("Enter CSV filename: ")
    cleaned = read_and_clean_csv(filename)
    # Output cleaned data
    output_file = 'cleaned_' + filename
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['post_text', 'likes', 'shares', 'hour', 'weekday']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in cleaned:
            writer.writerow(row)
    print(f" A cleaned dataset with structured features for sentiment/engagement analysis.")
if __name__ == "__main__":
    main()