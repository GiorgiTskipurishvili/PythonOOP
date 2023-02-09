"""
1. შექმენით კლასი Product, ინიციალიზაციის ფუნქციაში განუსაზღვრეთ ორი ატრიბუტი:
დასახელება და წონა. კლასს გადაუტვირთეთ შეკრების ოპერატორი, ისე რომ შეკრების შედეგად შეიკრიბოს მხოლოდ წონები.
 კლასს გადაუტვირთეთ ტოლობის ოპერატორი(==). ტოლობა უნდა დადგინდეს კლასის ატრიბუტით: სახელი. შექმენით კლასის
  რამდენიმე ობიექტი აჩვენეთ რომ ფუნქციონალი გამართულად მუშაობს.
"""
class Product:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight

    def __eq__(self, other):
        if isinstance(other,Product):
            return self.name == other.name
        return False

p1 = Product("Banana", 2.5)
p2 = Product("Orange", 4)
p3 = Product("Banana", 5)
print(p1+p2)
print(p1 == p2) 
print(p1 == p3)
