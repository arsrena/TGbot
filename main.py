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

# test
x = data_quote
y = x.data['BTC']['quote']['USD']['price']
round_price = round(y, 2)
print(round_price)
# процентное изменение цены
x1 = cmc.cryptocurrency_listings_latest()
y1 = x1.data[0]['quote']['USD']['percent_change_1h'] 
print(y1, '%')


bot = telebot.TeleBot('5654043644:AAHJ-rFpzwvzkjehr2tWg4FzksoG81WmGiI')

# @bot.message_handler()
# def get_user_text (message):
#     bot.send_message(message.chat.id, message, parse_mode='html')

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


# @bot.message_handler(content_types=['text'])
# def all_messages(message):
#     bot.send_message(chat_id=226048369, text='тестовое сообщение')

@bot.message_handler(content_types='text')
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot in ['Bitcoin','Ethereum','Tether', 'USD Coin', 'BNB'] :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton(f'{get_message_bot} Price')
        btn2 = types.KeyboardButton(f' {get_message_bot} Price change')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text=f"{get_message_bot}", reply_markup=markup)
   
    elif get_message_bot == 'Bitcoin Price':
        data_quote = cmc.cryptocurrency_quotes_latest(symbol='BTC', convert='USD')
        price_btc = data_quote.data['BTC']['quote']['USD']['price']
        round_price = round(price_btc, 2)
        bot.send_message(message.chat.id, f'{round_price} $')
        
    elif get_message_bot == 'Ethereum Price':
        data_quote = cmc.cryptocurrency_quotes_latest(symbol='ETH', convert='USD')
        price_eth = data_quote.data['ETH']['quote']['USD']['price']
        round_price = round(price_eth, 2)
        bot.send_message(message.chat.id, f'{round_price} $')

    elif get_message_bot == 'Tether Price':
        data_quote = cmc.cryptocurrency_quotes_latest(symbol='USDT', convert='USD')
        price_usdt = data_quote.data['USDT']['quote']['USD']['price']
        round_price = round(price_usdt, 2)
        bot.send_message(message.chat.id, f'{round_price} $')

    elif get_message_bot == 'USD Coin Price':
        data_quote = cmc.cryptocurrency_quotes_latest(symbol='USDC', convert='USD')
        price_usdc = data_quote.data['USDC']['quote']['USD']['price']
        round_price = round(price_usdc, 2)
        bot.send_message(message.chat.id, f'{round_price} $')

    elif get_message_bot == 'BNB Price':
        data_quote = cmc.cryptocurrency_quotes_latest(symbol='BNB', convert='USD')
        price_bnb = data_quote.data['BNB']['quote']['USD']['price']
        round_price = round(price_bnb, 2)
        bot.send_message(message.chat.id, f'{round_price} $')

    elif get_message_bot == 'Bitcoin Price change':
        lastest = cmc.cryptocurrency_listings_latest()
        lastest_bnb1 = round(lastest.data[0]['quote']['USD']['percent_change_1h'],3)
        lastest_bnb2 = round(lastest.data[0]['quote']['USD']['percent_change_24h'], 3)
        lastest_bnb3 = round(lastest.data[0]['quote']['USD']['percent_change_7d'], 3)
        bot.send_message(message.chat.id, f'За 1 час: {lastest_bnb1} %\n'
                                        f'За 24 часа: {lastest_bnb2} %\n'
                                        f'За 7 дней: {lastest_bnb3} %\n') 
                                    
    elif get_message_bot == 'Ethereum Price change':
        lastest = cmc.cryptocurrency_listings_latest()
        lastest_bnb1 = round(lastest.data[1]['quote']['USD']['percent_change_1h'],3)
        lastest_bnb2 = round(lastest.data[1]['quote']['USD']['percent_change_24h'], 3)
        lastest_bnb3 = round(lastest.data[1]['quote']['USD']['percent_change_7d'], 3)
        bot.send_message(message.chat.id, f'За 1 час: {lastest_bnb1} %\n'
                                        f'За 24 часа: {lastest_bnb2} %\n'
                                        f'За 7 дней: {lastest_bnb3} %\n') 
        
    elif get_message_bot == 'Tether Price change':
        lastest = cmc.cryptocurrency_listings_latest()
        lastest_bnb1 = round(lastest.data[2]['quote']['USD']['percent_change_1h'],3)
        lastest_bnb2 = round(lastest.data[2]['quote']['USD']['percent_change_24h'], 3)
        lastest_bnb3 = round(lastest.data[2]['quote']['USD']['percent_change_7d'], 3)
        bot.send_message(message.chat.id, f'За 1 час: {lastest_bnb1} %\n'
                                        f'За 24 часа: {lastest_bnb2} %\n'
                                        f'За 7 дней: {lastest_bnb3} %\n') 

    elif get_message_bot == 'USD Coin Price change':
        lastest = cmc.cryptocurrency_listings_latest()
        lastest_bnb1 = round(lastest.data[3]['quote']['USD']['percent_change_1h'],3)
        lastest_bnb2 = round(lastest.data[3]['quote']['USD']['percent_change_24h'], 3)
        lastest_bnb3 = round(lastest.data[3]['quote']['USD']['percent_change_7d'], 3)
        bot.send_message(message.chat.id, f'За 1 час: {lastest_bnb1} %\n'
                                        f'За 24 часа: {lastest_bnb2} %\n'
                                        f'За 7 дней: {lastest_bnb3} %\n') 
    
    elif get_message_bot == 'BNB Price change':
        lastest = cmc.cryptocurrency_listings_latest()
        lastest_bnb1 = round(lastest.data[4]['quote']['USD']['percent_change_1h'],3)
        lastest_bnb2 = round(lastest.data[4]['quote']['USD']['percent_change_24h'], 3)
        lastest_bnb3 = round(lastest.data[4]['quote']['USD']['percent_change_7d'], 3)
        bot.send_message(message.chat.id, f'За 1 час: {lastest_bnb1} %\n'
                                        f'За 24 часа: {lastest_bnb2} %\n'
                                        f'За 7 дней: {lastest_bnb3} %\n') 

    elif get_message_bot == 'Назад':
        menu (message)

    else:
          bot.send_message(message.chat.id, 'Ошибка') 




@bot.message_handler(content_types='text')
def send_message(bot, job):
    text = 'Это тестовое сообщение'
    bot.sendMessage(chat_id=user[357330578], text=text)


# @bot.callback_query_handler(func=lambda call: True)
# def query_handler(call):

#     bot.answer_callback_query(callback_query_id=call.id)
#     answer = ''
#     if call.data == 'Курс Bitcon':
#         answer = data_quote.data['BTC']['quote']['USD']['price']
#     else:
#         answer = 'ошибка'

#     bot.send_message(call.message.chat.id, answer)

    


bot.polling(none_stop=True)
