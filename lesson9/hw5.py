catalogue = []
catalogue.append({

    "Название": "Война и мир",

    "Автор": "Лев Толстой",

    "Год": 1869
}),
catalogue.append({

    "Название": "Преступление и наказание",

    "Автор": "Федор Достоевский",

    "Год": 1866
}),
catalogue.append({

    "Название": "Первый учитель",

    "Автор": "Чингиз Айтматов",

    "Год": 1988
}),
catalogue.append({

    "Название": "Тополек мой в красной косынке",

    "Автор": "Чынгыз Айтматов",

    "Год": 1964
}),
catalogue.append({

    "Название": "Swaroop",

    "Автор": "A Byte of Python",

    "Год": 2020
})
while True:
    print(f"Меню каталога.\n1.Вывод списка всех книг\n2.Добавление книги в каталог\n3.Выход")
    menu = input()
    if menu == "3":
        break
    elif menu == "1":    
        for book in catalogue:
            print(f"Название: {book['Название']}")
            print(f"Автор: {book['Автор']}")
            print(f"Год: {book['Год']}")      
    elif menu == "2":
        name = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги:")
        catalogue.append({
            "Название":name,
            "Автор": author,
            "Год": year
        })
        print("Книга успешна добавлена.")