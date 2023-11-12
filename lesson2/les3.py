a = int(input())
sym = input()
b = int(input())

if sym == "+":
    c = a + b
elif sym == "-":
    c = a - b
elif sym == "*":
    c = a * b
elif sym == "**":
    c = a ** b
else:
    c = a / b
print(c)

a = 5
b = 14
if a > 3 and b > 15:
    print('hello')
if a > 10 or b > 25:
    print('hi')
if not a > 10:
    print('grrr')   
