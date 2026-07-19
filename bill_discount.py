bill = int(input("Enter Bill Amount: "))

if bill > 5000:
    discount = bill * 10 / 100
    print("Discount:", discount)
else:
    print("No Discount")
