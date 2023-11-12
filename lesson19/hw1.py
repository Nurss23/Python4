# 1 января 1900 года - понедельник.

# В апреле, июне, сентябре и ноябре 30 дней. В феврале 28 дней, в високосный год - 29. В остальных месяцах по 31 дню.

# Високосный год - любой год, делящийся нацело на 4, однако последний год века (м) является високосным в том и только том случае, если делится на 400.

# Сколько воскресений выпадает на первое число месяца в двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?

import calendar
 
cnt = 0
for year in range (1901, 2000+1):
    for month in range (1, 13):
        if calendar.monthrange(year, month)[0] == 6:
            cnt += 1
 
print(cnt)
                 

v = []
age_r = list(range(1901, 2001))

for v_year in range(1904, 2000+1, 4):
    v.append(v_year)

for year in range(1901, 2000+1): 
    if year % 4 ==0:
        v.append(year)

print(len(age_r))