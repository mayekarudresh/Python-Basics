class one1:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.salary = int(input("Enter your salary: "))

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


h=one1()
h.display()