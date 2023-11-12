from class_bot import TelegramBot

token = "6932137138:AAF-egQQenDYrANZHC12aNHC3ab9xdc4yUk"
bot = TelegramBot(token)

chat_id = "1377778651" #id
## chat_id = "270623373" #Kaium baike

##Метод отправки сообщения
# bot.send_message(chat_id, "Hello from bot oop Nurs")

#Метод спама
# bot.sync_chats()
#метод спама
# bot.spam("test Nurs")


##excel
file_name = "test_bot.xlsx"
bot.create_chats_excel(file_name)

##excel spam
bot.spam_f_excel("test Nurss")
## print from excel


# #Метод отправки фото
# photo_url = "https://leonardo.osnova.io/5569a907-bbcf-5657-9fcb-a472aa78165f/-/preview/2100/-/format/webp/"
# bot.send_photo(chat_id, photo_url)

# #Метод отправки стикер
# sticker_id = "CAACAgIAAxkBAAEKlidlN4DeBfiK1qOz5NxJhxGlwN0JBwACLgEAAgz5TQwnK05SbaXRmjAE"
# bot.get_sticker(chat_id, sticker_id)


# print(bot.get_last())