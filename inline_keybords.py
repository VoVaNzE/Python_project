from aiogram.utils.keyboard import InlineKeyboardBuilder
from random import choice
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot
from aiogram.types import Message
                      

koshelok = 0

znachkis = ['💎' , '🗿', '💵', '🎰', '🥚', '☠️', '💤']
targets = []
for znack in znachkis:
    targets.append(znack*3)

def get_inline_keybords():
    kb = InlineKeyboardBuilder()
    callback_data = choice(znachkis) + choice(znachkis) + choice(znachkis)
    global koshelok
    kb.button(text='Игровой автомат 🎰',callback_data=callback_data)
    if callback_data in targets:
        koshelok += 1
    kb.button(text='Магагзин🏦', callback_data= keybord_handler)
    return kb.as_markup()

def get_inline_keybords1():
    kb = InlineKeyboardBuilder()
    if koshelok >= 1:
        koshelok = koshelok - 1
        callback_data = 'Поздравляю! Теперь вы можете расслабиться'
    else:
        callback_data = 'У вас не хватает денег :('
    kb.button(text='Расслабляющий напиток🧉 - стоит 1₽', callback_data=callback_data)

async def keybord_handler(msg: Message, bot: Bot):
    await msg.answer("Салам! Я бот, где ты можешь получить зависимость к крутке слотов! Начинаем?",reply_markup=get_inline_keybords1())   