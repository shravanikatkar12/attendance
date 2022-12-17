class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def accept(self,name,rollno):
        ob = Student(name,rollno)