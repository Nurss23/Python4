nums = [6, 2, 88, 23, 0, -5, 30, 9, 20, 10, 6, 56, -7]
a = []
b = []
for i in nums:
    if 0 == i % 3 and not i == 0:
        a.append(i)
    if 0 == i % 5 and not i == 0:
        b.append(i)
print(a ,b)
