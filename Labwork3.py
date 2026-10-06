import numpy as np
import math
class student:
    def __init__(self, student_id, name, dob,marks):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
    def input_marks(self, course_id, mark):
        round_mark = math.floor(mark * 10) / 10
        self.marks[course_id] = round_mark
    def calculate_gpa(self, all_courses):
        cid = []
        c_credits = []
        student_marks = []
        for c in all_courses:
            mark = self.marks.get(c.course_id)
            if mark is not None:
                cid.append(c.course_id)
                c_credits.append(c.credits)
                student_marks.append(mark)
        if not student_marks:
            return 0.0
        student_array = np.array(student_marks)
        credits_array = np.array(c_credits)
        weighted_sum = np.sum(student_array * credits_array)
        gpa = weighted_sum / np.sum(credits_array)
        return round(gpa, 2)
class course:
    def __init__(self,course_id,name,credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits
class manager:
    def __init__(self):
        self.students = []
        self.courses = []
    def input_student(self):
        n = int(input("Enter the number of students: "))
        for i in range(n):
            print("Enter details for student:")
            student_id = input("Enter Id: ")
            name = input("Enter Name: ")
            dob = input("Enter Date of Birth (DD_MM_YYYY): ")
            self.students.append(student(student_id, name, dob, {}))
    def input_courses(self):
        n = int(input("Enter the number of courses: "))
        for i in range(n):
            print("Enter details for course:")
            course_id = input("Enter Id: ")
            name = input("Enter Name: ")
            credits = float(input("Enter Credits: "))
            self.courses.append(course(course_id, name,credits))
    def input_marks(self):
        self.list_courses()
        cid = input("Enter the course id -> mark: ")
        if not any(c.course_id == cid for c in self.courses):
            print("Course not found.")
            return
        for stu in self.students:
            mark = float(input(f"Enter mark for student {stu.name} ({stu.student_id}): "))
            stu.input_marks(cid, mark)
    def list_students(self):
        for s in self.students:
            print(f"ID: {s.student_id}, Name: {s.name}, DOB: {s.dob}")
    def list_courses(self):
        for c in self.courses:
            print(f"ID: {c.course_id}, Name: {c.name}")
    def add_stu(self, name, dob, student_id):
        self.students.append(student(student_id, name, dob, {}))
    def add_course(self, name, course_id, credits): 
        self.courses.append(course(course_id, name, credits))
    def sort_students_gpa(self):
        self.students.sort(key=lambda s: s.calculate_gpa(self.courses), reverse=True)
        for s in self.students:
            gpa = s.calculate_gpa(self.courses)
            print(f"ID: {s.student_id} | Name: {s.name} | GPA: {gpa}")
if __name__ == "__main__":
    manager = manager()
    manager.input_student()
    manager.input_courses()
    manager.input_marks()
    manager.sort_students_gpa()



