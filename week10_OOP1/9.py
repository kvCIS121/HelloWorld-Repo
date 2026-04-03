# Create a Student class.
# A Student has
#  A name
#  A major
#  A GPA

# A Student can do
#  introduce themselves
#  study for exam

# You should write getters and setters for each of the instance variables.

# An introduction should be of the form: Hi, I’m name. I’m studying major.
# eg. Hi. I’m Maria. I’m studying Computer Science

# Studying for an exam should increase the GPA by 0.2 points. (up to a maximum of 4.0)
# It should be of the form:
# I’m hitting the books! My GPA increased from old GPA to new GPA.
# eg. I’m hitting the books! My GPA increased from 3.5 to 3.7.

class Student:
    # Constructor
    def __init__(self, name, major, GPA):
        self.name = name
        self.major = major
        self.gpa = GPA
    
    # Getter
    def get_name(self):
        return self.name
    def get_major(self):
        return self.major
    def get_gpa(self):
        return self.gpa
    
    # Setter
    def set_name(self, new_name):
        self.name = new_name
    def set_major(self, new_major):
        self.major = new_major
    def set_gpa(self, new_gpa):
        self.gpa = new_gpa

    # Method
    def introduction(self):
        print(f'Hi. I am {self.name}. I am studying {self.major}.')
    
    def exam_increase(self):
        new_gpa = self.gpa + 0.2
        
        if new_gpa > 4.0:
            new_gpa = 4.0
        
        print(f'I am hitting the books! My GPA increased from {self.gpa} to {round(new_gpa, 1)}')
        self.set_gpa(new_gpa)

student1 = Student('Kong', 'Computer Engineering', 3.1)

student1.introduction()
student1.exam_increase()