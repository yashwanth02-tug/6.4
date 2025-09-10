def discount(price, category):
    if category == "student":
        return price * 0.9 if price > 1000 else price * 0.95
    elif price > 2000:
        return price * 0.85
    return price

print("Total Price:", 1000 + 1500)
print("Discounted Price:", discount(1000 + 1500, "student"))