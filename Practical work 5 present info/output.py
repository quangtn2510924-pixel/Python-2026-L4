def list_students(students):
    for s in students:
        print(f"ID: {s.student_id}, Name: {s.name}, DOB: {s.dob}")
def list_courses(courses):
    for c in courses:
        print(f"ID: {c.course_id}, Name: {c.name}, Credits: {c.credits}")
def show_student_gpa(students, courses):
    sorted_students = sorted(students, key=lambda s: s.calculate_gpa(courses), reverse=True)
    for s in sorted_students:
        gpa = s.calculate_gpa(courses)
        print(f"ID: {s.student_id} | Name: {s.name} | GPA: {gpa}")