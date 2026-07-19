class Employee:
    def getDetails(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def showDetails(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

e = Employee()
e.getDetails(1, "Amit", 50000)
e.showDetails()