n = 4000000
res = 2
num_1 = 1
num_2 = 2
f = num_1 + num_2 # 3
while f < n:
    num_1 = num_2      
    num_2 = f       
    f = num_1 + num_2  
    if f % 2 == 0:
        res += f
print(res)

# num_1 = 1
# num_2 = 1
# i = 0
# while i < 1000:
#     f_sym = num_1 + num_2
#     num_1 = num_2
#     num_2 = f_sym
#     i += 1
# print(num_2)
def fib(num):
    for i in range(num-1):
        if i == 0:
            num_1 = 1
            num_2 = 2
        else:
            f_sym = num_1 + num_2
            num_1 = num_2
            num_2 = f_sym
    return f_sym
num = 6
res = fib(num)
print(res)