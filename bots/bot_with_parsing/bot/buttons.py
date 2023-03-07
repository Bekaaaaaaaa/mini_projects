from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from parsing.db_utils import get_pages

def get_Keyboard():
    pages = get_pages()


    pages_Keyboard = InlineKeyboardMarkup()

    buttons = []
    for page in pages:
        button = InlineKeyboardButton(page, callback_data=page)
        buttons.append(button)

    pages_Keyboard.add(*buttons)
    return pages_Keyboard