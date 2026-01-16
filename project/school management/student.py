from person import Person
from school import School


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self._id = None
        self.classroom = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def calculate_final_grade(self):
        total = 0
        for g in self.subject_grade.values():
            total += School.grade_to_value(g)
        self.grade = School.value_to_grade(total / len(self.subject_grade))
