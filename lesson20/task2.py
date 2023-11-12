from openpyxl import load_workbook

file_name = "students.xlsx"
excel = load_workbook(file_name)
page = excel["Лист1"]

commands = {
    "1" : "Показать студентов",
    "2" : "Показать оценки",
    "3" : "Средняя оценка"
}

print("Выберете комнаду:")
for key,value in commands.items():
    print(key,value)
input_value = input()

if input_value == "1":
    for cell in page["A"]:
        if cell.row == 1:
            continue
        print(cell.value)

if input_value == "2":
    for cell in page["B"]:
        if cell.row == 1:
            continue
        print(cell.value)
elif input_value == "3":
    # 1
    sm = 0
    qty = 0
    for cell in page["B"]:
        if cell.row == 1:
            continue
        sm += cell.value
        qty += 1
    print(sm / qty)
    # 2
    marks = [cell.value for cell in page["B"] if cell.row != 1]
    print(sum(marks) / len(marks))
# a = 0
# if input_value == "3":
#     for cell in page["B"]:
#         if cell.row == 1:
#             continue
#         a += cell.value
#         b = len(page["B"])
# b -= 1
# res = a / b
# print(res)