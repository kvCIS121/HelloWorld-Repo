class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    def get_major(self):
        return self.major
    
    def set_major(self, new_major):
        self.major = new_major

    def __str__(self):
        return f'Student name: {self.name}, major: {self.major}'
    
class Course:
    def __init__(self, course_name, course_number):
        self.course_name = course_name
        self.course_number = course_number
        self.students = []  

    def get_course_number(self):
        return self.course_number
    
    def set_course_number(self, new_course_number):
        self.course_number = new_course_number

    def add_student(self, student):
        self.students.append(student)

    def show_student_enrollment(self):
        for student in self.students:
            print(student)
    
    def __str__(self):
        return f'Course name: {self.course_name}, Course number: {self.course_number}. There are {len(self.students)} enrolled currently.'

#creating student objects
student1 = Student('km', 'Computer Engineering')
student2 = Student('Aiden', 'Civil Engineering')
student3 = Student('Phillip', 'Mechanical Engineering')

#creating course object
course1 = Course('CIS', '121')

#adding students to the course
course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)

#printing the results
course1.show_student_enrollment()
print(course1)