class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def display(self):
        print(f"Name: {self.name}, Roll Number: {self.roll}")

n=int(input("Enter number of students: "))
students = []
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    roll = input(f"Enter roll number of student {i+1}: ")
    student = Student(name, roll)
    students.append(student)
for student in students:
    student.display()
