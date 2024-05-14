from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def after_start_buttons():
    btn1 = KeyboardButton(text='Sherik kerak')
    btn2 = KeyboardButton(text='Ish joyi kerak')
    btn3 = KeyboardButton(text='Hodim kerak')
    btn4 = KeyboardButton(text='Ustoz kerak')
    btn5 = KeyboardButton(text='Shogird kerak')

    design = [
        [btn1, btn2],
        [btn3, btn4],
        [btn5]
    ]

    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
