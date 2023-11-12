while True:
    v_year = int(input("Введите год: "))
    if v_year == 0:
        break
    elif (v_year % 4 == 0 and v_year % 100 != 0) or v_year % 400 == 0:
        print(f"{v_year} является високосным годом")
    else:
        print(f"{v_year} не является високосным годом")