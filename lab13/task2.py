def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."
    except IOError as e:
        return f"Error reading file '{filename}': {e}" 
print(read_file("existing_file.txt"))
print(read_file("missing_file.txt"))
print(read_file("/root/forbidden_file.txt"))
