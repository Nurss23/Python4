def lis_age(age):
    res = [i for i in age if i >= 18 and i <= 27]
    return res
age = [15, 18, 20, 25, 30, 40]
print(lis_age(age))

def euler(num):
    res_2 = [i for i in list(range(1,num+1)) if i % 3 == 0 or i % 5 == 0]
    return sum(res_2)
num = 1000
print(euler(num))

def first():
    print("Первая функция")
def second():
    print("Начало второй функции")
    first()
    print("Конец второй функции")
def three():
    print("Функция 3 старт")
    first()
    second()
    print("конец 3 функции")

# def four():
#     print("Фантастическая функция 4")
#     four()
    
first()
second()
three()