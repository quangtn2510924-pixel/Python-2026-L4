import numpy as np
import math

class Student:
    def __init__(self, student_id, name, dob, marks=None):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = marks if marks is not None else {}

    def input_marks(self, course_id, mark):
        round_mark = math.floor(mark * 10) / 10
        self.marks[course_id] = round_mark

    def calculate_gpa(self, all_courses):
        c_credits = []
        student_marks = []
        for c in all_courses:
            mark = self.marks.get(c.course_id)
            if mark is not None:
                c_credits.append(c.credits)
                student_marks.append(mark)
        if not student_marks:
            return 0.0
        student_array = np.array(student_marks)
        credits_array = np.array(c_credits)
        weighted_sum = np.sum(student_array * credits_array)
        gpa = weighted_sum / np.sum(credits_array)
        return round(gpa, 2)