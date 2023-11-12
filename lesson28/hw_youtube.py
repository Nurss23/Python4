def calculate_earnings(lst_bloger, dollar):
    for k,v in  lst_bloger[0].items():
        print(f"Блогер: {k}") 
        for i, vl in v.items():
            earnings = round(vl[1] / 1000 * 0.50,2)
            print(f"за видео: {vl[0]}, {vl[1]}, заработал: {earnings} долларов или {earnings * dollar} сом")

lst_bloger = [{"apple_tree_girl_unboxing" : {"1" : ["buildihg", 77000],"2" : ["pixel_8", 51000], "3" : ["iphone_15", 359000], "4" : ["AYAENO", 107000], "5" : ["Samsung", 450000]},
"MrBeast" : {"1": ["Скважина", 5000000], "2" : ["Лазерный_лабиринт", 83000000], "3" : ["Дом", 126000000], "4" : ["Ловушка", 146000000], "5" : ["Машина", 163000000]},      
"ГОЛОС АНТОНЕНКО" : {"1": ["Шон Стрикленд", 92000], "2": ["Том Аспиналл", 96000], "3" : ["Джастин Гейджи", 238000], "4" : ["Чейл Сонен", 72000], "5" : ["Бенил Дариуш",17000]},   
"Peter McKinnon" : {"1" : ["Youtube",121000], "2" : ["Ultimate camera",93000], "3" : ["new camera",151000], "4" : ["social media",320000], "5" : ["camera", 148000]},
"CaseyNeistat" : {"1" : ["New career", 84000], "2" : ["Jew", 1300000], "3" : ["NYC",4500000], "4" : ["Changed",100000], "5" : ["vlog camera", 1400000]},
}]
dollar = 89

calculate_earnings(lst_bloger,dollar)