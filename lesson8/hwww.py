dct_products = {
    "яблоко": {"цена": 1.0, "количество": 100},
    "банан": {"цена": 0.5, "количество": 50},
    "апельсин": {"цена": 1.2, "количество": 70}
}
print('Добро пожаловать в магазин!')

while True:
    product = input().lower()
    if product == 'выход':
        break    
    if product in dct_products:
        product_info = dct_products[product]
        print(f'Цена {product_info["цена"]}, Кол-во {product_info["количество"]}')
        print('Введите следующий продукт: ')       
    else:
        print("Продукт отсутствует в магазине.")
print("Спасибо за покупки! До свидания!")

################################################################
# v2
# if product in dct_products:
#         product_info = dct_products[product]
#         print(f'Цена {product_info["цена"]}, Кол-во {product_info["количество"]}')
#         print('Введите следующий продукт: ')       
#     else:
#         print("Продукт отсутствует в магазине.")


#     elif product in dct_products:
#         print(dct_products[product])
#         print('Введите следующий продукт: ')  