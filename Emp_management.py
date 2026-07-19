salary = [25000,30000,28000,35000]

print("Employees salaries")

for i in salary:

    print(i)

    total = 0

    for i in salary:
        total = total + i
    print("total salary:",total)
