class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def show(self):
        field = [['#' for j in range(self.a)] for i in range(self.b)]
        for row in field:
            for cell in row:
                print(cell, end='')
            print()
            
figure_1 = Rectangle(7, 4)
figure_1.show()

class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = "#"
    def show(self):
        for i in range(self.b):
            if i == 0 or i == self.b - 1:
                for j in range(self.a):
                    print(self.c, end='')
            else:
                print(self.c, end='')
                for j in range(1, self.a - 1):
                    print(' ', end='')
                print(self.c, end='')
            print()
            
figure_1 = Rectangle(7, 4)
figure_1.show()