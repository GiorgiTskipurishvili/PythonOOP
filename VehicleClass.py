"""
1. შექმენით კლასი Vehicle. განუსაზღვრეთ ინიციალიზაციის ფუნქცია. განუსაზღვრეთ შემდეგი ატრიბუტი:
ტიპი. განუსაზღვრეთ მეთოდი info, რომელიც დაბეჭდავს Vehicle-ის ტიპს. დაიცავით ენკაფსულაციის პრინციპი.
კლასს შეუქმენით გეთერები და სეთერები.
"""

class Vehicle:
    def __init__(self,type):
        self._type = type

    def info(self):
        return f"Type of Vehicle: {self._type}"

if __name__ == '__main__':
    v1 = Vehicle("Audi")
    v2 = Vehicle("Mercedes")
    v3 = Vehicle("BMW")
    v4 = Vehicle("Volvo")
    v5 = Vehicle("Tesla")
    print(v1.info())
    print(v2.info())
    print(v3.info())
    print(v4.info())
    print(v5.info())
