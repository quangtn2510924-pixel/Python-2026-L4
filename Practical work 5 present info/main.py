import os
import pickle
import gzip
from input import input_students, input_courses, input_marks_for_students
from output import list_students, list_courses, show_student_gpa
from domain.student import Student
from domain.courses import Course
DATA_FILES = ["students.txt", "courses.txt", "marks.txt"]
ARCHIVE_NAME = "students.dat"
def decompress_data():
    """Kiểm tra và giải nén file students.dat nếu tồn tại"""
    if os.path.exists(ARCHIVE_NAME):
        try:
            with gzip.open(ARCHIVE_NAME, "rb") as f:
                data = pickle.load(f)
                for filename, content in data.items():
                    with open(filename, "w") as txt_file:
                        txt_file.write(content)
            print("Đã phát hiện và giải nén dữ liệu từ students.dat thành công!")
            return True
        except Exception as e:
            print(f"Lỗi khi giải nén file: {e}")
    return False
def compress_and_exit():
    """Nén các file dữ liệu thành students.dat trước khi thoát"""
    data = {}
    for filename in DATA_FILES:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data[filename] = f.read()
        else:
            data[filename] = ""
            
    try:
        with gzip.open(ARCHIVE_NAME, "wb") as f:
            pickle.dump(data, f)
        print(f"Đã nén dữ liệu thành công vào '{ARCHIVE_NAME}'. Tạm biệt!")
    except Exception as e:
        print(f"Lỗi khi nén file: {e}")

def load_data_from_txt():
    """Tải dữ liệu từ các tệp txt vào bộ nhớ chương trình"""
    students = []
    courses = []  
    # Load courses
    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    courses.append(Course(parts[0], parts[1], float(parts[2])))                 
    # Load students
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    students.append(Student(parts[0], parts[1], parts[2]))                 
    # Load marks
    if os.path.exists("marks.txt") and students:
        with open("marks.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    sid, cid, mark = parts[0], parts[1], float(parts[2])
                    for s in students:
                        if s.student_id == sid:
                            s.marks[cid] = mark                         
    return students, courses
def main():
    # Tự động giải nén dữ liệu cũ nếu có khi khởi động
    decompress_data()  
    # Tải dữ liệu sẵn có từ file txt vào bộ nhớ
    students, courses = load_data_from_txt()
    # Vòng lặp hiển thị menu tương tác từ 1 đến 6
    while True:
        print("\n================ STUDENT MANAGEMENT SYSTEM ================")
        print("1. Nhập danh sách sinh viên và các khóa học")
        print("2. Nhập điểm cho các sinh viên theo khóa học")
        print("3. Hiển thị danh sách các khóa học")
        print("4. Hiển thị danh sách sinh viên")
        print("5. Hiển thị bảng điểm và GPA của sinh viên (sắp xếp giảm dần)")
        print("6. Thoát chương trình (Nén dữ liệu vào students.dat)")
        print("===========================================================")
        choice = input("Chọn chức năng (1-6): ").strip()
        if choice == '1':
            print("\n--- NHẬP THÔNG TIN SINH VIÊN & KHÓA HỌC ---")
            students = input_students()
            courses = input_courses()
        elif choice == '2':
            print("\n--- NHẬP ĐIỂM ---")
            if not students or not courses:
                print("⚠️ Vui lòng nhập danh sách sinh viên và khóa học trước (Chọn 1).")
            else:
                input_marks_for_students(students, courses)
        elif choice == '3':
            list_courses(courses)
        elif choice == '4':
            list_students(students)
        elif choice == '5':
            show_student_gpa(students, courses)
        elif choice == '6':
            compress_and_exit()
            break
        else:
            print("❌ Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 6.")

if __name__ == "__main__":
    main()