import requests
from openpyxl import Workbook
server_respons = requests.get("https://jsonplaceholder.typicode.com/users")
data = server_respons.json()
names  = []
for element in data:
    names.append(element["name"])

new_excel_file = Workbook()
page = new_excel_file.active
for name in names:
    page.append([name])
    new_excel_file.save("user_table.xlsx")