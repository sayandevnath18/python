from person import Person
import random


class Teacher(Person):
    def teach(self):
        pass

    def evaluate_exam(self):
        return random.randint(0, 100)
