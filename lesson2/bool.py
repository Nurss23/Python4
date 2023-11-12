zp = float(input('зп: '))
otp = int(input('отп: '))

if zp >= 1000 and otp > 30:
    print('я согласен')
elif zp >= 1000 or otp > 30:
    print('я подумаю')
else:
    print('отказ')