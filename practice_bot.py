import telebot
from telebot import types

token = "6715365901:AAG4Uq0uJwFJnW88xrE0arcBY6y8FwbTC00"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def main(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    greeting = (
        f"Привет! {first_name}, {last_name}"
        if last_name is not None
        else f"Привет! {first_name}"
    )

    bot.send_message(message.chat.id, greeting)


@bot.message_handler(commands=["info"])
def mane1(message):
    bot.send_message(
        message.chat.id,
        "<b>Идиот,</b> <em><u> Иди нахуй со своей информацией</u></em>",
        parse_mode="html",
    )


@bot.message_handler(commands=["site"])
def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(
        text="легенда", url="https://www.youtube.com/watch?v=dy_DASt7hDs"
    )
    keyboard.add(url_button)
    bot.send_message(
        message.chat.id,
        "Переходи по ссылке",
        reply_markup=keyboard,
    )


@bot.message_handler()
def text(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    greeting = (
        f"Привет! {first_name}, {last_name}"
        if last_name is not None
        else f"Привет! {first_name}"
    )

    bot.send_message(message.chat.id, greeting)


bot.polling(none_stop=True)
