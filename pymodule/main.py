import telebot
import cpp_module as cpp
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

#TODO: добавить возможность писать кириллицей. Разобраться с проблемой конверсии форматов сторк (UTF - 8 coder exception)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Этот бот предназначен для шифрования/кодирования сообщений.\
                Чтобы зашифровать сообщение, введите команду /encode.\
                Чтобы расшифровать сообщение, введите команду /decode.")
_message = ""
_key = ""

def encrypt(message):
    global _message, _key
    bot.send_message(message.from_user.id,cpp._encrypt(_message,_key))

def decrypt(message):
    global _message, _key
    bot.send_message(message.from_user.id,cpp._decrypt(_message,_key))


def _print():
    global _message,_key
    print(f"Message: {_message},key {_key}")

def get_key_encrypt(message):
    global _key
    _key = message.text
    _print()
    encrypt(message)

def get_message_encrypt(message):
    bot.send_message(message.from_user.id,"Введите пароль")
    global _message
    _message = message.text
    bot.register_next_step_handler(message,get_key_encrypt)

def get_key_decrypt(message):
    global _key
    _key = message.text
    _print()
    decrypt(message)

def get_message_decrypt(message):
    bot.send_message(message.from_user.id,"Введите пароль")
    global _message
    _message = message.text
    bot.register_next_step_handler(message,get_key_decrypt)


    




# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == '/encode':
        bot.send_message(message.from_user.id,"Введите текст для зашифровывания")
        bot.register_next_step_handler(message,get_message_encrypt)
        global _message,_key
    elif message.text == '/decode':
        bot.send_message(message.from_user.id,"Введите зашифрованный текст")
        bot.register_next_step_handler(message,get_message_decrypt)
    else:
        bot.send_message(message.from_user.id,"Начните с ввода команды /start.")
        





bot.infinity_polling()