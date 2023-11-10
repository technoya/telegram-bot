import telebot

# Replace 'YOUR_TOKEN' with your actual bot token
bot = telebot.TeleBot('6831277971:AAFxb3fAHSqSqSIXAROMKFm7xflEBa1uHv4')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your Telegram bot. new bot")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
