import telebot
from time import sleep
from excel_file import ExcelFile

TOKEN = "6932137138:AAF-egQQenDYrANZHC12aNHC3ab9xdc4yUk"
chat_id = "1377778651"
tb = telebot.TeleBot(TOKEN)
excel_object = ExcelFile("infbot.xlsx")


while True:
    print("updating...")

    # синхронизация сообщений
    matrix = []
    for update in tb.get_updates():
        matrix.append([
            update.update_id,
            update.message.text,
        ])    
    excel_object.write_cells("messages", matrix)

    # обработка сообщений
    messages = excel_object.get_messages()
    theme_names = excel_object.get_theme_names()
    theme_numbers = excel_object.get_theme_numbers()
    for message, value in messages.items():
        if value["status"] != "+":
            if value["text"] == "/list":
                tb.send_message(chat_id, theme_names)
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                lst = []
                for number in theme_numbers:
                    btn = telebot.types.KeyboardButton(number)
                    lst.append(btn)
                markup.add(*lst)
                tb.send_message(chat_id, theme_names, reply_markup=markup)
            elif value["text"] in theme_numbers:
                theme_info = excel_object.get_theme_info(value["text"])
                tb.send_message(chat_id, theme_info)
                # with open(img_path, 'rb') as img_file:
                #     tb.send_photo(chat_id, img_file)
            value["status"] = "+"

    # сохраняем сообщения
    excel_object.update_messages(messages)
    sleep(3)