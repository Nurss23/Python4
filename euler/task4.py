num = 1

for i in range(99, 1000):
    for j in range(99, 1000):
        mult = i * j
        if str(mult) == str(mult)[::-1]:
            if mult > num:
                num = mult
print(num)