import os
import telebot
from telebot import types
import main

token = '5373945655:AAFtR2O_zRhPK1wpZoyFoPhBIO-5TRp0ybk'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Скидки в АТБ")
    item2 = types.KeyboardButton("Скидки в РОСТ")
    item3 = types.KeyboardButton("Скидки в АШАН")
    item4 = types.KeyboardButton("Скидки в ЧУДО")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Выберите супермаркет:', reply_markup=markup)

# @bot.message_handler(commands=['button'])
# def button_message(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton("Кнопка")
#     item2 = types.KeyboardButton("Кнопка")
#     item3 = types.KeyboardButton("Кнопка")
#     item4 = types.KeyboardButton("Кнопка")
#     markup.add(item1, item2, item3, item4)
#     bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Скидки в АТБ":
        bot.send_message(message.chat.id, "Please wait...")
        send_data(message.chat.id)

    # start_buttons = ['Скидки АТБ Харьков', 'Узнать что нового?']
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*start_buttons)
    # keyboard.add(*start_buttons1)
    # message.answer('Hi, Milord! ')
    # message.answer('Please select a Button', reply_markup=keyboard)


# @dp.message_handler(Text(equals='Скидки АТБ Харьков'))
# def moscow_city(message: types.Message):
#     message.answer('Please waiting...')
#     chat_id = message.chat.id
#     send_data(city_code='2398', chat_id=chat_id)  # city_code='2398',
#
#
# @dp.message_handler(Text(equals='Узнать что нового?'))
# def moscow_city(message: types.Message):
#     message.answer('Ничего интересного здесь пока нет...')


def send_data(chat_id):
    file = main.collect_data()
    bot.send_document(chat_id=chat_id, document=open(file, 'rb'))
    os.remove(file)


if __name__ == '__main__':
    bot.infinity_polling()
