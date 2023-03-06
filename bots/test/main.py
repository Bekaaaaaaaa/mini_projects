import telebot
from decouple import config

token = config('TOKEN')

token = '6177239965:AAHw5Vm3QBAkH_NSDNpi4enCDYj0lOCkOQE'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'привет')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIBSdkBXYWKieDoSD5ZVQPodYHnShqiQACvwkAAvzT4EowsTPJ5F5ibi4E')
    bot.send_photo(message.chat.id, 'https://news.store.rambler.ru/img/192a21629c70669f1fc2048e7d26058f?img-format=auto&img-1-resize=height:355,fit:max&img-2-filter=sharpen')

@bot.message_handler(content_types=['text'])
def aa(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'алейкум')
    else:
        bot.send_message(message.chat.id, 'напиши <привет>')


@bot.message_handler(content_types=['sticker'])
def  bb(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)

bot.polling()