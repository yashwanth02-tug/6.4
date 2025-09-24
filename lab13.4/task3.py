student_scores = {"Alice": 85, "Bob": 90}
score = student_scores.get("Charlie")
if score is not None:
    print(score)
else:
    print("Not Found")
