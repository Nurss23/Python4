import math
from datetime import datetime, time
import random

# n_fact = 5
# cos_pi, factorial_, math_e = math.cos(math.pi), math.factorial(n_fact), math.e
# print(f"Косинус (пи)= {cos_pi}\nЧисло 'e'= {math_e}\nФакториял числа {n_fact}= {factorial_}")

def math_func(cos_pi, factorial_, math_e):
    print(f"Косинус (пи)= {cos_pi}\nЧисло 'e'= {math_e}\nФакториял числа {n_fact}= {factorial_}")

n_fact = 5
math_func(cos_pi = math.cos(math.pi) , factorial_ = math.factorial(n_fact), math_e = math.e)

def func_timenow(time_now):
    print(f"Текущее время: {time_now}")

# time_now = datetime.now().time()
func_timenow(time_now= datetime.now().time())


def func_random(qnty_n):
    li = []
    n = 0
    while n != qnty_n:
        rnd = random.randint(1,20)
        li.append(rnd)
        n += 1
    chc = random.choice(li)
    print(li)
    print(chc)

# qnty_n = 5
func_random(qnty_n= 5)