num = int(input())

if num > 0:
    res = "число положительное"

elif num < 0:
    res = "число отрицательное"

else:
    res = "число равно 0"

if num == 0:
    res_2 = "не является натуральным числом"

elif num % 2 == 0:
    res_2 = "четное"

else:
    res_2 = "не четное"

print(f"{num}- {res},{res_2}")