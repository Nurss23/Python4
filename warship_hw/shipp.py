from sea0 import Sea
from sea1 import render

#  класс кораблей
class Ship:
    is_alive = True

    def __init__(self, y, x):
        self.y = y
        self.x = x
    
    def __repr__(self):
        if self.is_alive:
            return "s"
        else:
            return " "