class Fruit:
    sweet = True
    mass = 150

    def eat(self):
        self.mass = 0 
        print(self.mass)

class Apple(Fruit):
    color_options = ["red", "green"]

    def __init__(self,color):
        if color in self.color_options:
            print(color) 

class Orange(Fruit):
    color = "orange"

    def make_juice(self):
        self.juice = self.mass / 2
        print(self.juice)

fruit = Fruit()
fruit.eat()
apple = Apple("red")
orange = Orange()
orange.make_juice()



class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def show(self):
        field = [['#' for j in range(self.b)] for i in range(self.a)]
        for row in field:
            print(row[0],end='')
        print()
            # for cell in row:
            #     print(cell, end='')
        for cell in range(0,len(row), len(row)-1):
            print(cell, end='')
        print()
        
figure_1 = Rectangle(7, 4)
figure_1.show()