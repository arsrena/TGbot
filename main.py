import telebot
from telebot import types

# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# import json

# api_key = '7c1a3096-1d3a-4e5f-bb48-d4cb62fda73e'

# from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

# cmc = CoinMarketCapAPI(api_key)
  
# r = cmc.cryptocurrency_info(symbol='BTC')

# print(r)

bot = telebot.TeleBot('5654043644:AAHJ-rFpzwvzkjehr2tWg4FzksoG81WmGiI')


@bot.message_handler(commands=['start'])
def start (message):
    send_mess = f"Привет, {message.from_user.first_name}"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('биток')
    btn2 = types.KeyboardButton('Ethereum')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)   

@bot.message_handler(commands=['btc'])
def btc (message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт/курс Bitcoin", url="https://coinmarketcap.com/currencies/bitcoin/"))
    bot.send_message(message.chat.id, 'Курс Bitcoin', reply_markup=markup)

@bot.message_handler(commands=['eth'])
def eth (message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт/курс Ethereum", url="https://coinmarketcap.com/currencies/ethereum/"))
    bot.send_message(message.chat.id, 'Курс Ethereum', reply_markup=markup)

@bot.message_handler(content_types='text')
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == 'биток':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт/курс Bitcoin", url="https://coinmarketcap.com/currencies/bitcoin/"))
        bot.send_message(message.chat.id, 'Курс Bitcoin', reply_markup=markup)
    
    elif get_message_bot == 'Ethereum':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт/курс Ethereum", url="https://coinmarketcap.com/currencies/ethereum/"))
        bot.send_message(message.chat.id, 'Курс Ethereum', reply_markup=markup)   

    else:
          bot.send_message(message.chat.id, 'Ошибка') 



bot.polling(none_stop=True)
