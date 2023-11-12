from openpyxl import load_workbook

excel_file = load_workbook("user_table.xlsx")
page = excel_file["Sheet"]

print(page["A7"].value)

page["A11"] = "Жанар Айылчиев"
excel_file.save("user_table.xlsx")

page["B11"] = "Nurs"
excel_file.save("user_table.xlsx")