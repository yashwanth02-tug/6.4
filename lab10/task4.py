def process_scores(scores):
    if not scores:
        print("The list of scores is empty.")
        return

    print("Average:", sum(scores) / len(scores))
    print("Highest:", max(scores))
    print("Lowest:", min(scores))

my_scores = [85, 92, 78, 65, 95, 88, 70]
process_scores(my_scores)