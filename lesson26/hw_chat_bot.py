while True:
    chat = input("Добро пожаловать!")
    if chat == "exit":
        break
    if chat == str(): # " " с chat[-1] не работает
        print("Как классно, когда ты молчишь. Продолжай в том же духе!")
    elif chat.isupper():
        print("Успокойся")
    elif chat[-1] == "?":
        print("Конечно!")
    else:
        print("Ну и что")