stroka = input("Введите строку: ")
sym = input("Введите символ: ")
i = 0
pos = -1
while i < len(stroka): 
    if stroka[i] == sym:
        pos = i
        break
    i += 1
if pos != -1:
    print(f'{sym} найден на {pos +1} позиции')
else:
    print(f'{sym} отсутсвует')

