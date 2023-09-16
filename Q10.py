class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    
    def inputFields(self):
        self.empid = input("Enter Employee ID: ")
        self.name = input("Enter Employee Name: ")
        self.salary = input("Enter Employee Salary: ")

    def displayFields(self):
        print(f"Employee ID: {self.empid}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")
