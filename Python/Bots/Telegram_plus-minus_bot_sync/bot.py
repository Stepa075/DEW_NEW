import telebot
from telebot import types

import Variables
import config
import func

token = config.token
bot = telebot.TeleBot(token, threaded=False)
otvet = ""


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Число +- число =")
    item2 = types.KeyboardButton("Число +- число +- число =")
    # item3 = types.KeyboardButton("Скидки в АШАН")
    # item4 = types.KeyboardButton("Скидки в ЧУДО")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Выбери упражнение:', reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def message_reply1(message):
#     if message.text == "vfvf":
#         print("Yehoo!")
#     elif message.text.lower() == ("Выхо").lower():
#         start_message(message)
#     else:
#         message_reply(message)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    global otvet
    if message.text == "Число +- число +- число =":
        bot.send_message(message.chat.id, "Хорошо, начнем...")
        Variables.false = 0
        Variables.true = 0
        primer, otvet = func.start()
        bot.send_message(message.chat.id, primer)

    elif message.text.lower() == ("Выход").lower():
        start_message(message)

    elif func.control_int(message.text):
        if message.text == str(otvet):
            Variables.true += 1
            bot.send_message(message.chat.id, "Правильно!")
            bot.send_message(message.chat.id,
                             "Правильных ответов: " + str(Variables.true) + '\n' + "Неправильных ответов: " + str(
                                 Variables.false))
            print("cool")
            primer, otvet = func.start()
            bot.send_message(message.chat.id, primer)
        else:
            print("Fuck")
            Variables.false += 1
            bot.send_message(message.chat.id, "Неправильно!")
            bot.send_message(message.chat.id,
                             "Правильных ответов: " + str(Variables.true) + '\n' + "Неправильных ответов: " + str(
                                 Variables.false))
            primer, otvet = func.start()
            bot.send_message(message.chat.id, primer)

    else:
        bot.send_message(message.chat.id, "Введены не цифры и не команда!!")

    # bot.register_next_step_handler(message, is_answer_true(message, otvet))


# def is_answer_true(message, otvet):
#     if message.text == otvet:
#         bot.send_message(message.chat.id, "Правильно!")
#         primer, otvet = main.start()
#         bot.send_message(message.chat.id, primer)
#     else:
#         bot.send_message(message.chat.id, "Неправильно!")
#         primer, otvet = main.start()
#         bot.send_message(message.chat.id, primer)


# @bot.message_handler(content_types=['text'])
# def message_reply(message):
#     if message.text == "Число +- число +- число =":
#         bot.send_message(message.chat.id, "Хорошо, начнем...")
#         primer, otvet = main.start()
#         bot.send_message(message.chat.id, primer)
#
#         @bot.message_handler(content_types=["text"])
#         def proverka(message):
#             if message.text == otvet:
#                 bot.send_message(message.chat.id, "Правильно!")
#             else:
#                 bot.send_message(message.chat.id, "Неправильно!")
# send_data(message.chat.id)


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


# def send_data(chat_id):
#     file = main.collect_data()
#     bot.send_document(chat_id=chat_id, document=open(file, 'rb'))
#     os.remove(file)


if __name__ == '__main__':
    bot.infinity_polling()
