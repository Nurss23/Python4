# a = 1
# i = 18
# while i != 20:
#     if a % i == 0:
#         i += 1
#     else: 
#         i = 1
#         a += 1   
# print(a)

n = 20
lst_n = list(range(1,n+1))
num = 1
for i in lst_n:
    num *= i
numbers = []
for k in lst_n[::-1]:
    num /= k
    for i in lst_n[::-1]:
        if num % i != 0:
            num *= k
            break
        else:
            continue
    numbers.append(int(num))
print(min(numbers))
