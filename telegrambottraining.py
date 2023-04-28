import telebot
from telebot import types

bot = telebot.TeleBot('5855976846:AAGql9dbkQLUQ5RqHDDZVTsLrMs6VfR6gK8')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hi, <b>{message.from_user.first_name } <u>{message.from_user.last_name }</u></b>'
    bot.send_message(message.chat.id,mess,parse_mode="html")

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "hello":
#         bot.send_message(message.chat.id,"hi", parse_mode="html")
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode="html")
#     elif message.text == "photo":
#         photo = open('DSC_0794.JPG','rb')
#         bot.send_photo(message.chat.id,photo)
#     # else:
#     #     bot.send_message(message.chat.id, "i don't understand you", parse_mode="html")

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id,'Nice photo!')

@bot.message_handler(commands=['websiteY'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("websiteY",url="https://www.youtube.com/watch?v=VqChpNNYZ8Q&list=PLA0M1Bcd0w8yv0XGiF1wjerjSZVSrYbjh&index=3"))
    bot.send_message(message.chat.id, "սեխմիր այստեղ",reply_markup=markup)
@bot.message_handler(commands=['websiteW'])
def wevsite(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('websiteW',url="https://www.w3schools.com/python/python_ml_getting_started.asp"))
    bot.send_message(message.chat.id,"սեխմիր այստեղ",reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('help', url="https://www.youtube.com/watch?v=4zAThXFOy2c&list=PLjzeyhEA84sQKuXp-rpM1dFuL2aQM_a3S"))
    bot.send_message(message.chat.id, "սեխմիր այստեղ", reply_markup=markup)

@bot.message_handler(commands=['play'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('play',url='https://www.youtube.com/watch?v=Qd3E9_2ow9M'))
    bot.send_message(message.chat.id, 'սեխմիր այստեղ',reply_markup=markup)


bot.polling(none_stop=True)