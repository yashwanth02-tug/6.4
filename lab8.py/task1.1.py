def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operation"

# Example usage:
print(calculator(10, 5, '+'))  #Output: 15
print(calculator(10, 5, '-'))  # Output: 5
print(calculator(10, 5, '*'))  # Outp#ut: 50
print(calculator(10, 5, '/'))  # Output: 2.0
print(calculator(10, 0, '/'))  # Output: Error: Division by zero
print(calculator(10, 5, '%'))  # Output: Error: Invalid