lst = list(range(0,60,5))
for i, n in enumerate(lst):
    if n == 20:
        lst[i] = 200
print(sum(lst))

a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89]
for n in range(len(a)):
    a[n] = abs(round(a[n]))
    res = a[0] ** 3, a[-1] ** 3
print(a,res)