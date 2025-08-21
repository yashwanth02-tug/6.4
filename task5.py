class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

# Example usage:
if __name__ == "__main__":
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(initial_balance)

    while True:
        print("\nChoose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")