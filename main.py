import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot("6508154302:AAGX1pZ8HiCiN4fXl6fI42963Xd7PraLlP8")


@bot.message_handler(commands=["start"]) ###Я ввожу команду
def main(message):
    conn = sqlite3.connect("fail_dlya_bota.sql")
    cur = conn.cursor()

    cur.execute(''' CREATE TABLE IF NOT EXISTS users (
        id int auto_increment primary key,
        name varchar(50),
        password varchar 
    ) ''')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}, я чат-бот телеграмм канала Place Shop! "
                                      f"Напиши свое имя!")
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    pass

"""@bot.message_handler(commands=["start"]) ###Я ввожу команду
def main(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}, я чат-бот телеграмм канала Place Shop! ")
"""

@bot.message_handler(commands=["Go"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Подтвердить")
    markup.add(btn1)
    btn2 = types.KeyboardButton("Топ канал")
    btn3 = types.KeyboardButton("Сотрудничество")
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Нажимай на кнопочку!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text=="Подтвердить":
        bot.send_message(message.chat.id, "Заявка принята")
    elif message.text=="Топ канал":
        bot.send_message(message.chat.id, "Спасибки :)")
    elif message.text =="Сотрудничество":
        bot.send_message(message.chat.id, " Пиши в лс - gravyzz")



"""@bot.message_handler() ###Вводит пользователь какое то сообщение
def info(message):
    if message.test.lower()=="привет": bot.send_message(message.chat.id, f"Привет,{message.from_user.first_name}, я чат-бот телеграмм канала Place Shop!")
    elif message.test.lower()=="id":
        bot.reply_to(message, f"ID:{message.from_user.id}")"""


"""@bot.message_handler(commands=["NeRobot"])
def info(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Я не робот", callback_data="norobot")

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data=="norobot":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == "norobot":
        bot.edit_message_text("Edit", callback.message.chat.id, callback.message.message_id)"""


"""@bot.message_handler()
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(bot.send_message(message.chat.id, f"Привет,{message.from_user.first_name}, я чат-бот телеграмм канала Place Shop!")))
    bot.send_message(message.chat.id, f"Привет,{message.from_user.first_name}, я чат-бот телеграмм канала Place Shop!",reply_markup=markup)"""

"""@bot.message_handler()
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(bot.send_message(message.chat.id, ":)" )))"""

"""@bot.message_handler(commands=["go"])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(bot.send_message(message.chat.id, "Нажми на :)", callback_data="edit")))"""

bot.polling(none_stop=True)