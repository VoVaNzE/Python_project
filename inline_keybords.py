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
    kb.button(text='Информация🌐', callback_data='''
Игровой автомат 🎰
   Если вы получите 3 одинаковых смайлика(например 💎💎💎) получите 1₽
                        
Магазин🏦
    Тут вы можете закупиться разными предметами.
               
    Расслабляющий напиток🧉 с помощью него вы можете расслабиться
    от тяжёлой работы крутилщика слотов в НЕказино
              
    Допуск к колесу фортуны⭕️ теперь вы можете играть в колесо
    фортуны

    Мотивация💯 теперь вы можете ЗАМОТИВИРОВАТЬСЯ ИГРАТЬ В 
    НЕКАЗИНО

Колесо фортуны⭕️
    Если вам попадётся  ⬛️ ваш баланс, если 🟥 +10, 
    если 🟩 +100.Так что вы можеие и заработать 
    и всё потерять''')
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
    kb.adjust(1,1,1)
    return kb.as_markup()
