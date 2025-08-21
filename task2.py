# Function to print first 10 multiples of a number using a for loop
def print_multiples_for(n):
    for i in range(1, 11):
        print(n * i)

# Function to print first 10 multiples of a number using a while loop
def print_multiples_while(n):
    i = 1
    while i <= 10:
        print(n * i)
        i += 1

# Get input from the user
num = int(input("Enter a number: "))

# Example usage:
print("Using for loop:")
print_multiples_for(num)

print("\nUsing while loop:")
print_multiples_while(num)