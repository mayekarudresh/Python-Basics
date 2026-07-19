total = 0

for i in range(1, 6):
    marks = int(input(f"Enter marks of Student {i}: "))
    total += marks

average = total / 5

print("Average Marks:", average)