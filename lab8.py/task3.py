def get_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid value"
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# Example usage
try:
    marks = int(input("Enter marks (0-100): "))
    print("Grade:", get_grade(marks))
except ValueError:
    print("Invalid value")