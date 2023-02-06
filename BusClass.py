"""შექმენით კლასი Bus რომელიც იქნება Vehicle კლასის მემკვიდრე. განუსაზღვრეთ ინიციალიზაციის ფუნქცია.
განუსაზღვრეთ შემდეგი ატრიბუტები: ტიპი, ადგილების რაოდენობა, ფერი. განუსაზღვრეთ მეთოდი info,
 რომელიც კარგად წაკითხვად ფორმატში დაბეჭდავს Bus-ის შესახებ ინფორმაციას. დაიცავით ენკაფსულაციის პრინციპი.
  კლასს შეუქმენით გეთერები და სეთერები. შექმენით Bus კლასის რამდენიმე ობიექტი და
  აჩვენეთ რომ კლასის ფუნქციონალი გამართულად მუშაობს."""


class Vehicle:
    def __init__(self,type):
        self._type = type

    def get_type(self):
        return self._type
    def set_type(self,type):
        self._type = type

    def info(self):
        return f"Type: {self._type}"


class Bus(Vehicle):
    def __init__(self,type, num_of_seats, color):
        super().__init__(type)
        self._num_of_seats = num_of_seats
        self._color = color

    def get_num_of_seats(self):
        return self._num_of_seats
    def set_num_of_seats(self,num_of_seats):
        self._num_of_seats = num_of_seats

    def getcolor(self):
        return self._color
    def setcolor(self,color):
        self._color = color

    def info(self):
        super().info()
        return f"Tyoe of bus: {self._type}, Number of seats: {self._num_of_seats},  Color: {self._color}"

if __name__ == '__main__':
    bus1 = Bus("School Bus", 50, "Yellow")
    bus2 = Bus("Metro", 30, "White")
    print(bus1.info())
    print(bus2.info())
