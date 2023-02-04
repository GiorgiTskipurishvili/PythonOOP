""" 1) Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes."""

""" 2) Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle."""

""" 3) Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class."""

""" 4) Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped."""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def Perimeter(self):
        return (self.length + self.width)*2



    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.Perimeter()}")


""" 4) Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped."""
class Parallelepipede(Rectangle):
    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height = height

    def Volume(self):
        return self.length * self.width * self.height

    def display(self):
        super().display()
        print(f"Height: {self.height}")
        print(f"Volume: {self.Volume()}")

if __name__ == '__main__':
    # r = Rectangle(10,20)
    # r.display()

    p = Parallelepipede(10,20,30)
    p.display()
