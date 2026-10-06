
class student:
    def __init__(self, student_id, name, dob,marks):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
    def input_marks(self, course_id, mark):
        self.marks[course_id] = mark
class course:
    def __init__(self,course_id,name):
        self.course_id = course_id
        self.name = name
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
            self.courses.append(course(course_id, name))
    def list_students(self):
        for s in self.students:
            print(f"ID: {s.student_id}, Name: {s.name}, DOB: {s.dob}")
    def list_courses(self):
        for c in self.courses:
            print(f"ID: {c.course_id}, Name: {c.name}")
    def input_marks(self):
        self.list_courses()
        cid = input("Enter the course id -> mark: ")
        if not any(c.course_id == cid for c in self.courses):
            print("Course not found.")
            return
        for stu in self.students:
            mark = float(input(f"Enter mark for student {stu.name} ({stu.student_id}): "))
            stu.input_marks(cid, mark)
    def show_marks(self):
        self.list_courses()
        cid = input("Enter the course id to show marks: ")
        for s in self.students:
            if cid in s.marks:
                print(f"Student: {s.name}, Mark: {s.marks[cid]}")
            if not s.marks:
                print(f"Student: {s.name} has no marks for course {cid}.")
if __name__ == "__main__":
    manager = manager()
    manager.input_student()
    manager.input_courses()
    manager.list_students()
    manager.list_courses()
    manager.input_marks()
    manager.show_marks()
    



    