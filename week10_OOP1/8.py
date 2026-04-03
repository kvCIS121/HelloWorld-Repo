# Create an Employee class.
# An Employee has
#  A name
#  A title
#  A salary

# An Employee can do
#  a greeting
#  request raise

# You should write getters and setters for each of the instance variables.

# A greeting should be of the form: Hello. My name is name. I’m the title.
# eg. Hello. My name is Eugene. I’m the CEO.

# A raise request should request a 6% raise.
# It should be of the form: I’m currently making salary. I’d like new salary of new amount.
# eg. I’m currently making $100. I’d like new salary of $106

class Employee:
    # Constructor
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary
    
    # Getters
    def get_name(self):
        return self.name
    def get_title(self):
        return self.title
    def get_salary(self):
        return self.salary
    
    # Setters
    def set_name(self, new_name):
        self.name = new_name
    def set_title(self, new_title):
        self.title = new_title
    def set_salary(self, new_salary):
        self.salary = new_salary
    
    # Methods
    def greeting(self):
        print(f'Hello, my name is {self.name}. I am the {self.title}.')

    def request(self):
        new_salary = self.salary * 1.06
        print(f'I am currently making ${self.salary}. I would like a raise of 6%, which is ${new_salary}.')
        self.set_salary(new_salary)


employee1 = Employee('Steve Jobs', 'CEO', 100)
employee1.greeting()
employee1.request()

