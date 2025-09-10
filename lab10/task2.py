def find_common(a, b):
    return list(set(a) & set(b))

print(find_common([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]))