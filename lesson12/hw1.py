def sum_pow(num_1, num_2):
    res = num_1 ** num_2
    suma = 0
    for i in(str(res)):
        if i.isdigit():
            suma += int(i)
    return suma
print(sum_pow(num_1= 2, num_2 = 1000))