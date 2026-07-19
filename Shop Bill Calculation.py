total_bill = 0

for i in range(1, 6):
    price = float(input(f"Enter price of Item {i}: "))
    total_bill += price

print("Total Bill Amount:", total_bill)

