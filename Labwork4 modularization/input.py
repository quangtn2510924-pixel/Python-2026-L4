from domain.student import Student
from domain.courses import Course

def input_students():
    students = []
    n = int(input("Enter the number of students: "))
    for _ in range(n):
        print("Enter details for student:")
        student_id = input("Enter Id: ")
        name = input("Enter Name: ")
        dob = input("Enter Date of Birth (DD_MM_YYYY): ")
        students.append(Student(student_id, name, dob))
    return students

def input_courses():
    courses = []
    n = int(input("Enter the number of courses: "))
    for _ in range(n):
        print("Enter details for course:")
        course_id = input("Enter Id: ")
        name = input("Enter Name: ")
        credits = float(input("Enter Credits: "))
        courses.append(Course(course_id, name, credits))
    return courses

def input_marks_for_students(students, courses):
    print("Available courses:")
    for c in courses:
        print(f"ID: {c.course_id}, Name: {c.name}")
    cid = input("Enter the course id to input marks -> ")
    if not any(c.course_id == cid for c in courses):
        print("Course not found.")
        return
    for stu in students:
        mark = float(input(f"Enter mark for student {stu.name} ({stu.student_id}): "))
        stu.input_marks(cid, mark)