import telebot

token = "6932137138:AAF-egQQenDYrANZHC12aNHC3ab9xdc4yUk"
chat_id = "1377778651" #id
bot = telebot.TeleBot(token)

with open('py.png', 'rb') as photo:
    bot.send_photo(chat_id,photo)