import telebot
from telebot import types

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

api_key = '7c1a3096-1d3a-4e5f-bb48-d4cb62fda73e'

from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

cmc = CoinMarketCapAPI(api_key)
  
r = cmc.cryptocurrency_info(symbol='BTC')
data_quote = cmc.cryptocurrency_quotes_latest(symbol='BTC', convert='USD')

x = data_quote
y = x.data['BTC']['quote']['USD']['price']
round_price = round(y, 2)

print(round_price)

bot = telebot.TeleBot('5654043644:AAHJ-rFpzwvzkjehr2tWg4FzksoG81WmGiI')


@bot.message_handler(commands=['start'])
def start (message):
    send_mess = f"Привет, {message.from_user.first_name}"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Bitcoin')
    btn2 = types.KeyboardButton('Ethereum')
    btn3 = types.KeyboardButton('Tether')
    btn4 = types.KeyboardButton('USD Coin')
    btn5 = types.KeyboardButton('BNB')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)   

@bot.message_handler(commands=['menu'])
def menu (message):
    send_mess = 'Меню'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Bitcoin')
    btn2 = types.KeyboardButton('Ethereum')
    btn3 = types.KeyboardButton('Tether')
    btn4 = types.KeyboardButton('USD Coin')
    btn5 = types.KeyboardButton('BNB')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)   

@bot.message_handler(content_types='text')
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == 'Bitcoin':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Курс Bitcon')
        btn2 = types.KeyboardButton('График')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Bitcon", reply_markup=markup)

    elif get_message_bot == 'Ethereum':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Курс Ethereum')
        btn2 = types.KeyboardButton('График')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Ethereum', reply_markup=markup)

    elif get_message_bot == 'Tether':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Курс Tether')
        btn2 = types.KeyboardButton('График')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Tether', reply_markup=markup)
    
    elif get_message_bot == 'USD Coin':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Курс USD Coin')
        btn2 = types.KeyboardButton('График')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'USD Coin', reply_markup=markup)

    elif get_message_bot == 'BNB':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Курс BNB')
        btn2 = types.KeyboardButton('График')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'BNB', reply_markup=markup)

    elif get_message_bot == 'Курс Bitcon':
        data_quote = cmc.cryptocurrency_quotes_latest(symbol='BTC', convert='USD')
        # x = data_quote
        price_btc = data_quote.data['BTC']['quote']['USD']['price']
        round_price = round(price_btc, 2)
        # markup = types.InlineKeyboardMarkup()
        # markup.add(types.InlineKeyboardButton("Посетить веб сайт/курс Bitcoin", url="https://coinmarketcap.com/currencies/bitcoin/"))
        bot.send_message(message.chat.id, text=round_price)
        
    elif get_message_bot == 'Курс Ethereum':
        data_quote = cmc.cryptocurrency_quotes_latest(symbol='ETH', convert='USD')
        price_eth = data_quote.data['ETH']['quote']['USD']['price']
        round_price = round(price_eth, 2)
        bot.send_message(message.chat.id, text=round_price)

    elif get_message_bot == 'Курс Tether':
        data_quote = cmc.cryptocurrency_quotes_latest(symbol='USDT', convert='USD')
        price_usdt = data_quote.data['USDT']['quote']['USD']['price']
        round_price = round(price_usdt, 2)
        bot.send_message(message.chat.id, text=round_price)

    elif get_message_bot == 'Курс USD Coin':
        data_quote = cmc.cryptocurrency_quotes_latest(symbol='USDC', convert='USD')
        price_usdc = data_quote.data['USDC']['quote']['USD']['price']
        round_price = round(price_usdc, 2)
        bot.send_message(message.chat.id, text=round_price)

    elif get_message_bot == 'Курс BNB':
        data_quote = cmc.cryptocurrency_quotes_latest(symbol='BNB', convert='USD')
        price_bnb = data_quote.data['BNB']['quote']['USD']['price']
        round_price = round(price_bnb, 2)
        bot.send_message(message.chat.id, text=round_price)


    elif get_message_bot == 'Назад':
        menu (message)

    else:
          bot.send_message(message.chat.id, 'Ошибка') 

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id)
    answer = ''
    if call.data == 'Курс Bitcon':
        answer = data_quote.data['BTC']['quote']['USD']['price']
    else:
        answer = 'ошибка'

    bot.send_message(call.message.chat.id, answer)




bot.polling(none_stop=True)
