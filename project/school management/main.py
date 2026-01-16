from classroom import ClassRoom
from school import School
from student import Student
from subject import Subject
from teacher import Teacher


school = School("ABC School", "Dhaka")

# Classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Teacher
bangla_teacher = Teacher("Sonam")
english_teacher = Teacher("Raj")
science_teacher = Teacher("Dipok")

# Subjects
bangla = Subject("Bangla", bangla_teacher, 100, 33)
english = Subject("English", english_teacher, 100, 33)
science = Subject("Science", science_teacher, 100, 33)

eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(science)
nine.add_subject(bangla)
nine.add_subject(english)
nine.add_subject(science)
ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(science)

# Students
rahim8 = Student("Rahim")
karim8 = Student("Karim")
kamal8 = Student("Kamal")
rahim9 = Student("Rahim")
karim9 = Student("Karim")
kamal9 = Student("Kamal")
rahim10 = Student("Rahim")
karim10 = Student("Karim")
kamal10 = Student("Kamal")

rahim8.classroom = eight
karim8.classroom = eight
kamal8.classroom = eight
rahim9.classroom = nine
karim9.classroom = nine
kamal9.classroom = nine
rahim10.classroom = ten
karim10.classroom = ten
kamal10.classroom = ten

school.student_admission(rahim8)
school.student_admission(karim8)
school.student_admission(kamal8)

school.student_admission(rahim9)
school.student_admission(karim9)
school.student_admission(kamal9)

school.student_admission(rahim10)
school.student_admission(karim10)
school.student_admission(kamal10)

# Take Exam
eight.take_semester_final()
nine.take_semester_final()
ten.take_semester_final()

# Print Result
print(school)
print(eight.get_top_students())
print(nine.get_top_students())
print(ten.get_top_students())
