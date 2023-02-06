"""
Create a Python class Person with attributes: name and age of type string.
Create a display() method that displays the name and age of an object created via the Person class.
Create a child class Student  which inherits from the Person class and which also has a section attribute.
Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
Create a student object via an instantiation on the Student class and then test the displayStudent method.
"""

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self,name,age,section):
        super().__init__(name,age)
        self.section = section

    def displayStudent(self):
        return f"Name: {self.name}, Age: {self.age}, Section: {self.section}"

if __name__ == '__main__':
    s1 = Student("John Smith", 22, "A")
    s2 = Student("Arnold Depy", 25, "B")
    s3 = Student("Ele Diva", 21, "C")
    print(s1.displayStudent())
    print(s2.displayStudent())
    print(s3.displayStudent())
