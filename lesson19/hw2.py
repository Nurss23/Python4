class Animal:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(self.name,self.age)

    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        super().speak()
        return("Гав-гав!")
    
class Cat(Animal):

    def speak(self):
        super().speak()
        return("Мяу!")

class Cow(Animal):

    def speak(self):
        super().speak()
        return("Мууу!")

class Zoo():

    lst_name = []
    lst_age = []
    lst_speak = []

    def add_animal(self,n):

        self.lst_name.append(n.name)
        self.lst_age.append(n.age)
        self.lst_speak.append(n.speak())

    def list_animals(self):
        
        print(f"Животное: {self.lst_name[0]}, Возраст: {self.lst_age[0]}, Звук: {self.lst_speak[0]}")
        print(f"Животное: {self.lst_name[1]}, Возраст: {self.lst_age[1]}, Звук: {self.lst_speak[1]}")
        print(f"Животное: {self.lst_name[2]}, Возраст: {self.lst_age[2]}, Звук: {self.lst_speak[2]}")


dog = Dog("Барон", 3)
cat = Cat("Мурзик", 2)
cow = Cow("Буренка", 5)
zoo = Zoo()
zoo.add_animal(cat)
zoo.add_animal(dog)
zoo.add_animal(cow)
zoo.list_animals()