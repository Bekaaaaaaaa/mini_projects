import telebot
from decouple import config

token = config('TOKEN')

yes_sticker = 'CAACAgIAAxkBAAEIBY1kBYb6Ys_GmOspkM5TLTA3yD5OiwACjwkAAvtY4Uqw-_cO7HE0nC4E'
no_sticker = 'CAACAgIAAxkBAAEIBaRkBYitQBA9d71vxzo1DDlXwaPK2QACRAADJeuTHwZ6PBYan0PRLgQ'

bot = telebot.TeleBot(token)

# клавиатура
keyboard = telebot.types.ReplyKeyboardMarkup()
b1 = telebot.types.KeyboardButton('yes')
b2 = telebot.types.KeyboardButton('no') 
keyboard.add(b1, b2)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'любишь меня?', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'yes':
        bot.send_sticker(message.chat.id, yes_sticker)
    elif message.text == 'no':
        bot.send_sticker(message.chat.id, no_sticker)
    else:
        bot.send_message(message.chat.id, 'нажмите на кнопку')

    bot.register_next_step_handler(message, reply_to_button)



bot.polling()