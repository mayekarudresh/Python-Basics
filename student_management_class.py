class Student:

    def get_details(self):
        self.student_id = int(input("Enter Student ID: "))
        self.name = input("Enter Student Name: ")
        self.course = input("Enter Course Name: ")

        self.mark1 = int(input("Enter Marks 1: "))
        self.mark2 = int(input("Enter Marks 2: "))
        self.mark3 = int(input("Enter Marks 3: "))

    def calculate_percentage(self):
        self.percentage = (self.mark1 + self.mark2 + self.mark3) / 3

    def display_grade(self):
        if self.percentage >= 90:
            grade = "A+"
        elif self.percentage >= 75:
            grade = "A"
        elif self.percentage >= 60:
            grade = "B"
        elif self.percentage >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print("Grade:", grade)

    def display_details(self):
        print("\nStudent Details")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Percentage:", self.percentage)


# Object Creation
s1 = Student()

# Method Calls
s1.get_details()
s1.calculate_percentage()
s1.display_details()
s1.display_grade()