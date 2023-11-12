sea = []

#создаем пустое поле
for i in range(5):
    sea.append([])
    for j in range(5):
        sea[-1].append(" ")

#добавляем корабли
ships = 3
for k in range(ships):
    y = int(input(f"координата 'y' Корабля {k+1}"))
    x = int(input(f"координата 'x' Корабля {k+1}"))
    sea[y][x] = "s"

#начинаем игру
while ships:
    for row in sea:
        for cell in row:
            print(cell, end='')
        print()

    fire_point = input("Противник стреляет: ") 
    points_lst = fire_point.split()
    fire_y = int(points_lst[0])
    fire_y = int(points_lst[0])

    if sea[fire_y][fire_x] == "s":
        print("попал")
        sea[fire_y][fire_x] = " "
        ships -= 1
    else:
        print("мимо")
    