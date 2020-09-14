
def format_price(price):
    price = int(price)
    return (f"Цена: {price} руб.")
f = format_price(56.24)
print(f)