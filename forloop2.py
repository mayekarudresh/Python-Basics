total_salary = 0

for i in range(1, 6):
    salary = int(input(f"Enter salary of Employee {i}: "))
if salary > 30000:
    total_salary += salary

print("Total Salary:", total_salary)
