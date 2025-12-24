
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__marks = 0
        self.grade = 'F'

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            self.calculate_grade()
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")
    def get_marks(self):
        return self.__marks
    def calculate_grade(self):
        if self.__marks >= 90:
            self.grade = 'A'
        elif self.__marks >= 80:
            self.grade = 'B'
        elif self.__marks >= 70:
            self.grade = 'C'
        elif self.__marks >= 60:
            self.grade = 'D'
        elif self.__marks >= 50:
            self.grade = 'E'
        else:
            self.grade = 'F'    
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.__marks}")
        print(f"Grade: {self.grade}")
        print()

student1 = Student("Alice", 101)
student2 = Student("Bob", 102)
student3 = Student("Charlie", 103)  

student1.set_marks(95)      
student2.set_marks(76)
student3.set_marks(45)      

student1.show_details()
student2.show_details()
student3.show_details()

student4 = Student("David", 104)
student4.set_marks(110)  
student4.show_details()