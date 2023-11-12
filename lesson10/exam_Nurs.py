##################### Task 1
while True:
    num_1 = int(input("Введите первое число: "))
    num_2 = int(input("Введите второе число: "))
    sym = num_1 + num_2
    print(sym)
    if sym % 2 == 0:
        print("Сумма является четным числом")
    else:
        print("Сумма является нечетным числом")
###################### Task 2
# while True:
#     c_radius = int(input("Введите радиус окружности: ")) 
#     if c_radius > 0:
#         s = (3.14159265358979323846 * c_radius ** 2)
#         print(f"Площадь окружности: {s}")
#     else:
#         print("Радиус должен быть положительным числом")
######################### Task 3
# num = int(input("Введите число: "))
# n = 1
# while n <= num:
#     print(n)
#     n += 3
# print("цикл while")
# for i in range(1,num,4):
#     print(i)
# print("цикл for")
########################## Task 4
# students_dct = []
# i = 1
# inf_st = int(input("Введите количество студентов: "))
# print("Ввод информации о студентах: ")
# while i <= inf_st:
#     i += 1
#     name = input("Имя: ")
#     age = input("Возраст:")
#     students_dct.append({
#         "Имя" : name,
#         "Возраст": age
#     })
# print(students_dct)
############################ Task5
# num_1 = 0
# num_2 = 1
# i = 0
# while i < 999:
#     f_sym = num_1 + num_2
#     num_1 = num_2
#     num_2 = f_sym
#     i += 1
# print(num_2)

# a = 0
# num_1 = 1
# num_2 = 2
# while a < 1000:
#     f = num_1 + num_2 
#     num_1 = num_2      
#     num_2 = f        
#     a += 1
# print(num_2)