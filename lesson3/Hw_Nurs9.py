som = int(input("Введите свой финансовый баланс: "))
if som >0:
    print(f"Ваш баланс составляет {som} сом")
elif som <0: 
    print(f"Ваш долг составляет {som} сом")
else:
    print("У вас 0 сом")