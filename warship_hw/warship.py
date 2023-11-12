from sea0 import Sea
from sea1 import render
from shipp import Ship

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