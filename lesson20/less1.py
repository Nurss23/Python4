from openpyxl import load_workbook

file_name = "students.xlsx"
excel = load_workbook(file_name)
list_1 = excel["Лист1"] 
list_1["A2"] = "Bayaman"
list_1["B2"] = 100
list_1["A3"] = "Nurs"
list_1["B3"] = 60
list_1["A4"] = "Asan"
list_1["B4"] = 89
list_1["A5"] = "Ularbek"
list_1["B5"] =  95
excel.save(file_name)