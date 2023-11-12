import requests

server_respons = requests.get("https://jsonplaceholder.typicode.com/users")
print(server_respons.status_code)

data = server_respons.json()
print(data)
print(type(data))

names  = []
for element in data:
    names.append(element["name"])
print(names)

#запись в файл
with open("user.txt", "w") as users_file:
    for name in names:
        users_file.write(f"{name}\n")