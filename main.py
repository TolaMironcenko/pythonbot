import time
import telebot
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from telebot import types

token = '5123679189:AAHTMxCyOUwPSbaeof31m8SjRHVs4qKZci8'  # testbot
bot = telebot.TeleBot(token)

print('bot started')


def love(message, k=0):
    current = 0
    for i in range(k):
        bot.send_message(message.chat.id, "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
                                          "❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤️")
        print('ok' + str(current))
        current += 1
        time.sleep(2)


def googleparse(message, searchinput):
    k = 0
    for i in search(searchinput):
        print(str(k + 1) + " " + str(i))
        markup = types.InlineKeyboardMarkup()
        btnNum = types.InlineKeyboardButton(text="перейти по ссылке", callback_data=i)
        markup.add(btnNum)
        bot.send_message(message.chat.id, str(k + 1) + " " + str(i), reply_markup=markup)  # + " " + str(i))
        k += 1


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    bot.send_message(call.message.chat.id, "Собираем информацию о странице №" + call.message.text.split(' ')[0] + "...")
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    driver = webdriver.Chrome(options=opts)
    driver.get(call.data)
    time.sleep(1)
    driver.find_element(by=By.TAG_NAME, value='body')
    driver.get_screenshot_as_file("bot.png")
    driver.quit()
    time.sleep(1)
    bot.send_photo(call.message.chat.id, open('./bot.png', 'rb'))


@bot.message_handler(commands=['search', 'love'])
def start(message):
    if message.text.split(' ')[0] == '/search' and len(message.text.split(" ")) != 1:
        a = message.text.split(' ')
        a.pop(0)
        searchinput = ''
        for i in a:
            searchinput = searchinput + i + ' '
        print(searchinput)
        googleparse(message, searchinput)
    elif message.text.split(' ')[0] == '/search':
        bot.send_message(message.chat.id, "введите /search + 'поисковый запрос'")
    elif message.text.split(' ')[0] == '/love' and len(message.text.split(" ")) != 1:
        love(message, int(message.text.split(' ')[1]))
    elif message.text.split(' ')[0] == '/love':
        bot.send_message(message.chat.id, "введите /love + '(число) количество повторений'")


bot.infinity_polling()

print('bot stopped')
