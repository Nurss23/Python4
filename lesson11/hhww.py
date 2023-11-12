def is_leap(v_year):
    if (v_year % 4 == 0 and v_year % 100 != 0) or v_year % 400 == 0:
        y = "является високосным годом"
    else:
        y = "не является високосным годом"
    return y
v_year = 34264
is_leap_r = is_leap(v_year)
print(is_leap_r)