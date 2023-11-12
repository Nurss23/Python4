# import math

# def is_prime(x):
#     for i in range(3, int(math.sqrt(x)+1), 2):
#         if x % i == 0:
#             return False
#     return True

# y = 1
# counter = 1

# while counter != 10001:
#     y += 2
#     if is_prime(y):
#         counter += 1

# print(y)



def is_prime(x):
    for i in range(3, int(x ** 0.5)+1, 2):
        if x % i == 0:
            return False
    return True

y = 1
counter = 1

while counter != 10001:
    y += 2
    if is_prime(y):
        counter += 1
print(y)