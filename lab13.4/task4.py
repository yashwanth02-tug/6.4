operation = "multiply"
a, b = 5, 3
operations_map = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
}
result = operations_map.get(operation, lambda x, y: None)(a, b)

print(result)
