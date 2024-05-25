from aiogram.utils.keyboard import InlineKeyboardBuilder
from random import choice
from aiogram.utils.keyboard import InlineKeyboardBuilder
from product import Product
from store import store
                      
# znachkis = ['💎' , '🗿', '💵', '🎰', '🥚', '☠️', '💤']
znachkis = ['💎']
znachkis2 = ['⬛️']*7
znachkis3 = ['🟥']*5
znachkis4 =['🟩']+znachkis2+znachkis3
targets = []
for znack in znachkis:
    targets.append(znack*3)

for znack in znachkis4:
    targets.append(znack)

def get_inline_keybords():
    kb = InlineKeyboardBuilder()
    callback_data = choice(znachkis) + choice(znachkis) + choice(znachkis)

    if callback_data in targets:
        store.change_score(1)
    kb.button(text='Игровой автомат 🎰',callback_data=callback_data)
    kb.button(text='Магазин🏦', callback_data= 'Магазин')
    if store.dopysk == True:
        callback_data = choice(znachkis4)
    else:
        callback_data = 'У вас нету допуска :('

    if callback_data == '⬛️':
        store.score = 0
    if callback_data == '🟥':
        store.score = store.score + 10
    if callback_data == '🟩':
        store.score = store.score + 100
    kb.button(text='Колесо фортуны⭕️', callback_data=callback_data)
    callback_data = 'info'
    kb.button(text='Информация🌐', callback_data= callback_data)
    kb.adjust(2,2)
    return kb.as_markup()

def get_inline_keybords1():
    kb = InlineKeyboardBuilder()
    kb.button(text='Расслабляющий напиток🧉 - стоит 1₽', callback_data=Product(
        name='Расслабляющий напиток',
        price=1
    ))
    kb.button(text='Допуск к колесу фортуны⭕️ - стоит 10₽', callback_data=Product(
        name='Допуск к колесу фортуны',
        price=10
    ))
    kb.button(text='Мотивация💯 - стоит 5₽', callback_data=Product(
        name='Мотивация',
        price=5
    ))
    kb.button(text='Статус Билл Гейтса💸 - 1000000₽', callback_data=Product(
        name='Статус Билл Гейтса',
        price=1000000
    ))
    kb.button(text='Анекдот🎭 - 5₽', callback_data=Product(
        name='Анекдот',
        price=5
    ))
    kb.button(text='Капибара - 10₽', callback_data=Product(
        name='Капибара',
        price=15
    ))
    kb.adjust(1,1,1,1,1,1)
    return kb.as_markup()
 
