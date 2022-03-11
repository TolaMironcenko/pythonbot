import telebot
import time
from googlesearch import search

token = '1741158845:AAGGsDYJX6Q7IbZT3O1p5ERGOmgYbStMCRU'

bot = telebot.TeleBot(token)


def love(massage, k=0):
    current = 0
    for i in range(k):
        bot.send_message(massage.chat.id, "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤️")
        print('ok' + str(current))
        current += 1
        time.sleep(2)


def googleparse(massage, searchinput):
    for i in search(searchinput):
        bot.send_message(massage.chat.id, i)


@bot.message_handler(commands=['search', 'love'])
def start(massage):
    if massage.text.split(' ')[0] == '/search':
        a = massage.text.split(' ')
        a.pop(0)
        searchinput = ''
        for i in a:
            searchinput = searchinput + i + ' '
        print(searchinput)
        if searchinput == '':
            bot.send_message(massage.chat.id, "введите /search + 'поисковый запрос'")
        else:
            googleparse(massage, searchinput)
    if massage.text.split(' ')[0] == '/love':
        love(massage, int(massage.text.split(' ')[1]))


bot.polling()
