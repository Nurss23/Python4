# import telebot
# from time import sleep
# from excel import ExcelFile

# TOKEN = "6932137138:AAF-egQQenDYrANZHC12aNHC3ab9xdc4yUk" # свой токен
# chat_id = "1377778651" # свой id чата
# tb = telebot.TeleBot(TOKEN)
# excel_object = ExcelFile("cupss.xlsx")


# while True:
#     print("updating...")

#     # синхронизация сообщений
#     matrix = []
#     for update in tb.get_updates():
#         matrix.append([
#             update.update_id,
#             update.message.text,
#         ])    
#     excel_object.write_cells("messages", matrix)

#     # обработка сообщений
#     messages = excel_object.get_messages()
#     cup_names = excel_object.get_cup_names()
#     cup_names = excel_object.get_cup_price()
#     for message, value in messages.items():
#         if value["status"] != "+":
#             if value["text"] == "/list":
#                 cup_names = excel_object.get_cup_names()
#                 tb.send_message(chat_id, cup_names)
#             elif value["text"] == "/price":
#                 cup_names = excel_object.get_cup_price()
#                 tb.send_message(chat_id, cup_names)
#             value["status"] = "+"

#     # сохраняем сообщения
#     excel_object.update_messages(messages)
#     sleep(3)
