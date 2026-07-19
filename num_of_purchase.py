purchase = []

print("Enter 10 customer purchase amounts")

for i in range(10):
    amount = float(input("Enter purchase amount:"))

    purchase +=[amount]

    count = 0

    for i in range(10):
        if purchase[i] > 5000:
            count = count + 1

        print("\nPurchase Amount")
        for i in range(10):
            print(purchase[i])

            print("\nNumber of Purchases above 5000=",count)