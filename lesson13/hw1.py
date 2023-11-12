def extract_digits(txt):
    suma = [int(i) for i in txt if i.isdigit()]
    return suma
txt = "lsj94ksd231 9"
res = extract_digits(txt)
print(f"Вывод: {res}")
print(f"Сумма: {sum(res)}")

# def extract_digits(txt):
#     suma = [int(i) for i in txt if i.isdigit()]
#     print(f"Сумма: {sum(suma)}")
#     return suma
# print("Вывод:", (extract_digits(txt = "sj94ksd231 9")))

# def extract_digits(txt):
#     nums = []
#     for i in(txt):
#         if i.isdigit():
#             nums.append(int(i))
#     return nums
# txt = "lsj94ksd231 9"
# res = extract_digits(txt)
# print(f"Вывод: {res}")
# print(f"Сумма: {sum(res)}")