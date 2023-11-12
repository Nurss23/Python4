cup = int(input("Введите количество чашек : "))
if cup % 10 == 1 and cup != 11:
    print(f"{cup} чашка")
elif 2 <= cup % 10 <= 4 and not 12 <= cup <= 14:
    print(f"{cup} чашки")
else:
    print(f"{cup} чашек")   