students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78
}

# Add new student
students["Neha"] = 88

# Update marks
students["Amit"] = 82

# Display all students and marks
print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# Find topper
topper = max(students, key=students.get)

print("\nTopper Details")
print("Name:", topper)
