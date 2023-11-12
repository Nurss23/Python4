import requests
url = ("https://api.telegram.org/bot6450383163:AAHb6Do-tMkORRBWdQjAyZrXyWyq1-1teC0/")
respons = requests.get(f"{url}getUpdates")
data = respons.json()
chat_idd = (data["result"][-4]["message"]["chat"]["id"]) #chat id
chat_id = chat_idd
chat_id = 1377778651
text = "Привет, Нурс!"
requests.get(f"{url}sendMessage?chat_id={chat_id}&text={text}")

