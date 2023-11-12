# класс морей
class Sea:
    
    # создаём пустое поле/море
    def __init__(self, field_size):
        field = [[' ' for j in range(field_size)] for i in range(field_size)]
        self.field = field

    # функция отрисовки моря (рендер)
    def render(self):
        for row in self.field:
            for cell in row:
                print(cell, end='')
            print()


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
        
        
# генерация объектов
sea = Sea(5) # field_size

# добавляем корабли
ships = 3
for k in range(ships):
    y = int(input(f"координата 'y' корабля {k+1}: "))
    x = int(input(f"координата 'x' корабля {k+1}: "))
    ship_object = Ship(y, x)
    sea.field[y][x] = ship_object

# начинаем игру
while ships:
    # отрисовка моря
    sea.render()
    
    # ход противника
    fire_point = input("Противник стреляет: ") # 2 4
    points_list = fire_point.split() # ['2', '4']
    fire_y = int(points_list[0]) # 2 
    fire_x = int(points_list[1]) # 4

    # проверка попадания
    fired_cell = sea.field[fire_y][fire_x]
    if isinstance(fired_cell, Ship):
        print("попал")
        fired_cell.is_alive = False
        ships -= 1
    else:
        print("мимо")

print("End Game")