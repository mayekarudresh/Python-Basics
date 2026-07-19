class Employee:

    def get_data(self):
        self.emp_id = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.salary = float(input("Enter Basic Salary: "))

    def calculate_salary(self):
        hra = self.salary * 0.20
        da = self.salary * 0.10
        self.net_salary = self.salary + hra + da

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Net Salary:", self.net_salary)


e = Employee()
e.get_data()
e.calculate_salary()
e.display()