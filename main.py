import telebot 


bot = telebot.TeleBot('7938703166:AAG0bjlfcRiaeNBpy06EyFJCDEkjJNfBwjo')

@bot.message_handler(commands=['start'])

def welcome(message):
    bot.send_message(message.chat.id, 'Kir')

bot.polling()


