class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if not isinstance(name, str):
            raise ValueError("Item name must be a string.")
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        if name in self.items:
            self.items[name] += price
        else:
            self.items[name] = price

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"{name} not found in cart.")
        del self.items[name]

    def total_cost(self):
        return sum(self.items.values())