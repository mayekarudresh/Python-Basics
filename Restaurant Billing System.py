total = 0

while True:
    price = float(input("Enter Item Price (0 to Exit): "))

    if price == 0:
        break

    total += price

print("Total Bill =", total)