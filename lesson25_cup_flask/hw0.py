while True:
    num = input("Введите число: ")
    if num == "end":
        break
    for n in num.split():
        if n.isalpha():
            continue
        elif n.isdigit():
            print(int(n), type(int(n)))
    
while True:
    num = input("Введите число с плавающей точкой: ")
    if num == "end":
        break
    if "." in num:
        if num.isalpha():
            continue
        elif num.isalpha() and num.isdigit():
            continue
        else:
            res = float(num), type(float(num))
    else:
        continue
    print(res)