import telebot
from decouple import config

token = config('TOKEN')

yes_sticker = 'CAACAgIAAxkBAAEIBY1kBYb6Ys_GmOspkM5TLTA3yD5OiwACjwkAAvtY4Uqw-_cO7HE0nC4E'
no_sticker = 'CAACAgIAAxkBAAEIBaRkBYitQBA9d71vxzo1DDlXwaPK2QACRAADJeuTHwZ6PBYan0PRLgQ'

bot = telebot.TeleBot(token)

# клавиатура под сообщением
keyboard = telebot.types.InlineKeyboardMarkup()
b1 = telebot.types.InlineKeyboardButton('да', callback_data='yes')
b2 = telebot.types.InlineKeyboardButton('нет', callback_data='no')
keyboard.add(b1, b2)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'любишь меня?', reply_markup=keyboard)

# функция фильтр в данном случае разрешаются все сообщения 
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_sticker)



bot.polling()