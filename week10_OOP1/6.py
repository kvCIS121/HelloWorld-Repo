# Create a Course class.
# A Course has
#  course code
#  course name
#  instructor

# An Course can do
#  print_info

# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.
# Instantiate an instance of the class. You may pass any initial values of your choosing.
# Write a method called print_info, which prints in the form
# “[course code]: [course name] taught by [instructor]”
# example. “CIS101: Introduction to programming taught by Matt”.

class Course:
    # Constructor
    def __init__(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor
    
    # Getters
    def get_course_code(self):
        return self.course_code
    def get_course_name(self):
        return self.course_name
    def get_instructor(self):
        return self.instructor
    
    # Setters
    def set_course_code(self, new_course_code):
        self.course_code = new_course_code
    def set_course_name(self, new_course_name):
        self.course_name = new_course_name
    def set_instructor(self, new_instructor):
        self.instructor = new_instructor
    
    # Method
    def print_info(self):
        print(f'{self.course_code} {self.course_name} taught by {self.instructor}')
    
course1 = Course('CIS 121', 'Intro to Programming', 'Professor Priem')
course1.print_info()