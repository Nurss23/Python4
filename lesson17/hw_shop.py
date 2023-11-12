class Shop:

    def __init__(self,name):
        self.name = name
        self.dct_product = {}

    def add_product(self,product_name,price,quantity=1):

        if product_name in self.dct_product:
            self.dct_product[product_name] = price, self.dct_product[product_name][1] + quantity
        else:
            self.dct_product[product_name] = price,quantity
            print(f"Товар: {product_name} добавлен, цена- {price}")

    def get_product_info(self, product_name):
        
        if product_name in self.dct_product:
            print(f"{product_name}: цена- {self.dct_product[product_name][0]}, кол-во {self.dct_product[product_name][1]}")

    def buy_product(self, product_name, quantity):

        if product_name in self.dct_product:
                price, avalab_qnty = self.dct_product[product_name]
                if avalab_qnty >= quantity:
                    res = price * quantity
                    self.dct_product[product_name] = (price, avalab_qnty - quantity)
                    print(f"Вы купили {quantity} шт. товара {product_name} за {res} в магазине ")
                else:
                    print("Товара не достаточно или его нет в магазине.")
        else:
            print("Этого товара нет в магазине")

            

my_shop = Shop("Мой магазин")
my_shop.add_product("Хлеб", 1.5, 20) 
my_shop.add_product("Яйца", 3) 
my_shop.add_product("Молоко", 2, 3) 
my_shop.add_product("Молоко", 2, 1) 
my_shop.get_product_info("Яйца")
my_shop.buy_product("Молоко", 2)
my_shop.buy_product("Молоко", 2)
my_shop.buy_product("Молоко", 2)
my_shop.buy_product("Молоко", 8)
