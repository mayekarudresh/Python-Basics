salary = []

print("Enter salary of 5 employees:")

for i in range(5):
    s = int(input("Enter Salary: "))
    salary += [s]

count = 0

for i in range(5):
    if salary[i] > 40000:
        count = count + 1

print("Employees with salary above ₹40000 =", count)