def employee_ops(name, salary, raise_percent):
    print(f"emp: {name} salary: {salary}")
    salary += salary * raise_percent / 100
    print(f"emp: {name} salary: {salary}")
employee_ops("Alice", 50000, 10)