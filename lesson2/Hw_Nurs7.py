sch = int(input("Введите оценку за экзамен: "))
hw = int(input("Введите количество выполненных домашних заданий :"))
if sch >= 90 and hw >= 10:
    print("Отлично.")
elif sch >= 70 and hw >= 5:
    print("Хорошо.")
else:
    print("Удовлетворительно.")