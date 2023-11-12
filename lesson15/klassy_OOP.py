class Cat:
    paws = 4
    tail = 1
murzik = Cat()
print(type(murzik))

k = 10**3
def lucky(n):
    for i in range(1, k):
        if i == n:
            print(i,"Верно")
            break
num = 67
n = int(input())
print(lucky(n))

k = 1000000
def binary_search(num):
    q = 0 
    c = int( k / 2)
    step = c / 2
    while True:
        print(c)
        if c < num:
            print("Меньше")
            c = round(c + step)
        elif c > num:
            print("Больше")
            c = round(c - step)
        else:
            print(c, f"Верно! Кол-во шагов {q}")
            break
        step /= 2
        q += 1
n = int(input(f"Введите число от 1 до {k}: "))
binary_search(n)