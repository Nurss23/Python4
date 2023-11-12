user = input("Введите ваше имя: ")
money = int(input("Введите количество ваших денег: "))
inv = 1000

print(f"{user.title()}, ваше количество денег через 10 лет: {(inv * 10) + money}")