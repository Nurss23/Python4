lst_nick = ['Nurs', 'user2', 'Hskill']
while True:
    user = input('Введите ник: ')
    if user in lst_nick:
        print(f'Ты – свой. Приветствую, любезный {user}!')
        break
    else:
        print('Тут ничего нет. Еще есть вопросы?')