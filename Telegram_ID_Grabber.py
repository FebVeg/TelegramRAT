# Coded by FebVeg

import telebot

TOKEN = "YOUR API TOKEN"

bot = telebot.TeleBot(TOKEN)
ID = 123456789 # your ID for receive data log of id grabber

try:
    bot.send_message(ID, "ID GRABBER: *ONLINE*", parse_mode="Markdown")
except:
    print("You need to replace ID variable with your real telegram ID")
    print("BOT is started")

def get_data(message):
    user_name = message.chat.username
    user_id = message.chat.id
    user_cmd = message.text
    data = "======= USER =======" + "\nID: %s\nUsername: %s\nInput: %s\n" % (user_id, user_name, user_cmd)
    try:
        bot.send_message(ID, str(data))
    except:
        print("You need to replace ID variable with your real telegram ID")
    print(data)
        
@bot.message_handler(func=lambda message: True)
def id_grabber(message):
    get_data(message)

bot.polling()
