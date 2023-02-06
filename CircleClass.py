"""
1 - Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
2 - Define a Area() method of the class which calculates the area of the circle.
3 - Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
4 - Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not.
"""
import math
class Circle:
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r

    def Area(self):
        return math.pi * (self.r)**2

    def Perimeter(self):
        return 2 * math.pi * self.r

    """4 - Define a testBelongs() method of the class which allows to test whether
     a point A(x, y) belongs to the circle C(O, r) or not."""

    def testBelongs(self,x,y):
        return (x - self.a) **2 + (y - self.b)**2 <= self.r**2





if __name__ == '__main__':
    c=Circle(3,6,3)
    print(c.Area())
    print(c.Perimeter())
    print()
    print()
    print(c.testBelongs(3,4))
