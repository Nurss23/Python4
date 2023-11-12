from openpyxl import load_workbook

file_name = "students1.xlsx"
excel = load_workbook(file_name)
list_1 = excel["Лист1"] 
list_1["A1"] = "Имя"
list_1["B1"] = "Возраст"
list_1["A2"] = "Ali"
list_1["B2"] = 19
list_1["A3"] = "Nurs"
list_1["B3"] = 20
list_1["A4"] = "Asan"
list_1["B4"] = 17
list_1["A5"] = "Ularbek"
list_1["B5"] =  23
excel.save(file_name)