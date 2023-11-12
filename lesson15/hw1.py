name_1 = input("Введите имя: ")
name_2 = input("Введите фамилию: ")
num_plate = input("Введите номерной знак: ")
for num in range(len(num_plate)):
    if num_plate[0].isdigit():
        res = "у Вас новый образец."
    else:
        res = "у Вас старый образец."
print(f"{name_1.title()}, {name_2.title()}, {num_plate.upper()}- {res}")