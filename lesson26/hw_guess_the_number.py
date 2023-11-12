from random import randrange
random_number = randrange(10)
# print(random_number)

n = 0
print("Угадайте число")

while True:
    num = int(input())
    n += 1
    if 0 < num < 9:
        if num == random_number:
            print(f"Поздравляем! Вы угадали число {random_number} с {n} попытки.")
            break
        elif 0 < num >9:
                print("Введите число в диапазоне от 0 до 9.")
    else:
        print("Введите целое число от 0 до 9.")