# 3. Write a function that takes a dictionary, called exams, 
# containing the course grades of a student, and
# returns the name of the course with the minimal grade.
#   Examples:
    #   min_grade({ ”Physics”: 82, ”Math”: 65, ”History”: 75, ”Biology”: 95, ”English” : 87}) → ”Math”
    #   min_grade({ ”Chemistry”: 78, ”Algebra”: 88, ”History”: 72, ”Geography”: 85}) → ”History”
    #   min_grade({ ”Art”: 90, ”Music”: 92, ”Drama”: 89}) → ”Drama”

def min_grade(exams):
    course_name = ' '
    lowest_grade = 100
    
    for current_course, current_grade in exams.items():
        if current_grade < lowest_grade:
            lowest_grade = current_grade
            course_name = current_course
    return {course_name:lowest_grade}

exams1 = ({ 'physics': 82, 'math': 65, 'history': 75, 'biology': 95, 'english' : 87})
exams2 = ({ 'chemistry': 78, 'algebra': 88, 'history': 72, 'geography': 85})
exams3 = ({ 'art': 90, 'music': 92, 'drama': 89})

print(min_grade(exams1))
print(min_grade(exams2))
print(min_grade(exams3))