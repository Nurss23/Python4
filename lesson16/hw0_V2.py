class Car:
    def __init__(self,brand,year,color):
        self.brand = brand
        self.year = year
        self.color = color
        self.horsepower = 85 
    def get_auto(self):
        print(f"Бренд - {self.brand}, год выпуска - {self.year}, цвет - {self.color}")
    def get_year(self):
        print(f"Возраст авто - {2023 - self.year}")
    def add_horsepower(self):
        if self.brand not in ("Mers", "BMW", "Porshe"):
            print(f"{self.horsepower + 20} - лошадиных сил")
        else:            
            print(f"{self.horsepower + 40} - лощадиных")

mers = Car("Mers", 2000, "blue")
mers.get_auto()
mers.get_year()
mers.add_horsepower()

bmw = Car("BMW", 1995, "black")
bmw.get_auto()
bmw.get_year()
bmw.add_horsepower()

porshe = Car("Porshe", 1987, "red")
porshe.get_auto()
porshe.get_year()
porshe.add_horsepower()

auto1 = Car("Ferrari", 1999, "red")
auto1.get_auto()
auto1.get_year()
auto1.add_horsepower()