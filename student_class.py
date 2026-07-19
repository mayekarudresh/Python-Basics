class Student:
    def setData(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def displayData(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)

s = Student()
s.setData("Rahul", 101)
s.displayData()