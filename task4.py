def sum_to_n(n):
    """
    Calculate the sum of the first n natural numbers using a for loop.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Get input from the user
n = int(input("Enter a number: "))
print(sum_to_n(n))