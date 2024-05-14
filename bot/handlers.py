from aiogram import html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from bot.button.reply import after_start_buttons
from dispatcher import dp


@dp.message(CommandStart())
async def start_handler(msg: Message):
    help_text_header = f"{html.bold('Assalomu alaykum ')}" + f'{html.bold(msg.from_user.full_name)}\n'
    help_text_body = html.bold('UstozShogird kanalining rasmiy botiga xush kelibsiz!\n\n')
    help_text_footer = '/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!'
    full_text = help_text_header + help_text_body + help_text_footer
    await msg.answer(text=full_text, reply_markup=after_start_buttons())


@dp.message(Command('help'))
async def smth_handler(msg: Message):
    helper_text_header = 'UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali\n\n'
    helper_text_body = 'Bu yerda Programmalash bo`yicha\n #Ustoz, #Shogird,\n #oquvKursi, #Sherik,\n #Xodim va #IshJoyi'
    helper_text_footer = "\ntopishingiz mumkin.\n\nE'lon berish: @illegal_testing_bot\n\nAdmin: @UstozShogirdAdminBot"
    full_text = helper_text_header + helper_text_body + helper_text_footer
    await msg.answer(text=full_text)

@dp.message()
