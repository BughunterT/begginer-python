items = []
prices = []
total = 0

while True:
    item = input("enter the item (press q to quit):")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"enter {item} price: $"))
        items.append(item)
        prices.append(price)

print("-----your cart-----")
for item in items:
    print(item)

for price in prices:
    total = total + price

print(f"your total is ${total}")
