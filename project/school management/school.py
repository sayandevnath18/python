class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        student.classroom.add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"

    @staticmethod
    def grade_to_value(grade):
        return {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}[grade]

    @staticmethod
    def value_to_grade(value):
        if value >= 3.5:
            return "A"
        elif value >= 2.5:
            return "B"
        elif value >= 1.5:
            return "C"
        elif value >= 0.5:
            return "D"
        else:
            return "F"

    def __repr__(self):
        result = f"School Name: {self.name}\nAddress: {self.address}\n"
        for cname, classroom in self.classrooms.items():
            result += f"\nClassRoom: {cname}\n"
            for student in classroom.students:
                result += f"{student.name} - Final Grade: {student.grade}\n"
        return result
