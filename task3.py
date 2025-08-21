age = int(input("Enter your age: "))

if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teen")
elif 20 <= age <= 50:
    print("Adult")
elif age > 50:
    print("Senior")
else:
    print("Invalid age") 