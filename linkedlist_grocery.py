grocery = ["Rice", "sugar", "Milk", "Tea"]

print("shopping list")

for i in grocery:
    print(i)
    grocery.append("sugar")
    print("updated list")
    for i in grocery:
        print(i)
