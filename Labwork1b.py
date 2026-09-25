def input_student():
    n = int(input("Enter the number of students: "))
    students = []
    for i in range(n):
        print(f"Enter details for student {i + 1}:")
        id = input("Enter Id: ")
        name = input("Enter Name: ")
        dob = input("Enter Date of Birth (DD_MM_YYYY): ")
        stu = {"id": id, "name": name, "dob": dob}
        students.append(stu)
    return students
def num_courses():
    n = int(input("Enter the number of courses: "))
    courses = []
    for i in range(n):
        print(f"Enter details for course {i + 1}:")
        id = input("Enter Id: ")
        name = input("Enter Name: ")
        courses.append({"id": id, "name": name})
    return courses
def input_marks():
    if not courses:
        print("no courses , please enter courses first")
        return
    if not students:
        print("no students , please enter students first")
        return
    list_courses()
    course_id = input("Enter the course id -> mark: ")
    if not any(course['id'] == course_id for course in courses):
        print("Course not found.")
        return
    marks ={}
    if course_id not in marks:
        marks[course_id] = {}
    print("Enter marks for students:")
    for student in students:
        mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
        marks[course_id][student['id']] = mark
def list_courses():
    if not courses:
        print("No courses")
    for c in courses:
        print(f"Course ID: {c['id']}, Name: {c['name']}")
def student_list():
    if not students:
        print("No students")
    for s in students:
        print(f"Student ID: {s['id']}, Name: {s['name']}, Date of Birth: {s['dob']}")
def show_marks():
    if not marks:
        print("No marks in system")
    return
    list_courses()
    course_id = input("Enter the course id to show marks: ")
    if course_id in marks:
        id = student['id']
        for student in students:
            if student['id'] in marks[course_id]:
                print(f"Student ID: {student['id']}, Name: {student['name']}, Mark: {marks[course_id][student['id']]}")
            else:
                print(f"Student ID: {student['id']}, Name: {student['name']}, Mark: Not available")
def main():
    while True:
        print("\nMenu:")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. Show marks for a course")
        print("5. List all students")
        print("6. List all courses")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            students = input_student()
        elif choice == '2':
            courses = num_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            show_marks()
        elif choice == '5':
            student_list()
        elif choice == '6':
            list_courses()
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
    
    