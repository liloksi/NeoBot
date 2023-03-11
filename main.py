import telebot 
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import webbrowser



bot = telebot.TeleBot('6176257020:AAFHdQJbAPEXBQ-pUZl-6wRzCqNwCmC65xA')


category_buttons = InlineKeyboardMarkup()
category_buttons.add(InlineKeyboardButton('Криптовалюты', callback_data='crypto'))
category_buttons.add(InlineKeyboardButton('Валюты', callback_data='currencies'))
category_buttons.add(InlineKeyboardButton('Индексы', callback_data='index'))
category_buttons.add(InlineKeyboardButton('Товары', callback_data='products'))
category_buttons.add(InlineKeyboardButton('Акции', callback_data='stock'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Выберите категорию: ', reply_markup=category_buttons)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Привет! Я-телеграм бот.'
                                      'Моя основная задача - отправлять тебе актуальные цены на валюты.')
    
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://neocapital.info/')
    
@bot.message_handler(func=lambda message: True)
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')


bot.infinity_polling()

