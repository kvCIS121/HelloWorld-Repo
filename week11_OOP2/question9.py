class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_position(self):
        return self.position
    
    def set_position(self, new_position):
        self.position = new_position
    
    def __str__(self):
        return f'Employee(name = {self.name}, position = {self.position})'

class Department:
    def __init__(self, dept_name, budget):
        self.dept_name = dept_name
        self.budget = budget
        self.employees = []

    def get_budget(self):
        return self.budget
    
    def set_buget(self, new_budget):
        self.budget = new_budget
    
    def add_employee(self, employee):
        self.employees.append(employee)

    def is_large(self):
        employee = 0
        for employee in self.employees:
            if len(self.employees) >= 10:
                return True
            else:
                return False
    
    def show_staff_list(self):
        for employee in self.employees:
            print(employee)

    def __str__(self):
        return f'Department(dept_name = {self.dept_name}, budget = {self.budget})'

#creating employees object    
employee_1 = Employee('jeff', 'mixer')
employee_2 = Employee('inglis', 'mixer')
employee_3 = Employee('daniel', 'sheeter')

#creating department object
department_1 = Department('cookies', 1000)

#adding employees to the department
department_1.add_employee(employee_1)
department_1.add_employee(employee_2)
department_1.add_employee(employee_3)

#executing program
department_1.show_staff_list()
print(department_1)