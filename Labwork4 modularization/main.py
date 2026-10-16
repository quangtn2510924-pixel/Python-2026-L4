from input import input_students, input_courses, input_marks_for_students
from output import list_students, list_courses, show_student_gpa

def main():
    students = input_students()
    courses = input_courses()
    
    input_marks_for_students(students, courses)
    
    list_students(students)
    list_courses(courses)
    show_student_gpa(students, courses)

if __name__ == "__main__":
    main()