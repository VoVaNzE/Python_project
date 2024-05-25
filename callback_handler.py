from aiogram import Bot
from aiogram.types import CallbackQuery
from inline_keybords import get_inline_keybords, get_inline_keybords1
# from inline_keybords import koshelok
from store import store
from product import Product
from random import choice

anekdot = ['Книга получается хорошей, если автор действительно знает то, о чём пишет. Фильм получается хорошим, если сценарист, режиссёр, актёры хотя бы отчасти пережили то, о чём рассказывают. Поэтому лучше всего у киношников выходят фильмы про истеричных дегенератов, алкоголиков и проституток, а хуже всего - про добрых честных людей, хорошо делающих своё дело.', 'Не спрашивай у мужчины про его доходы, у женщины про возраст, у патриота, откуда у него американский паспорт.',  'Зачем пересаживать чиновников на отечественные автомобили, если они имеют право на бесплатный проезд в общественном транспорте?', 'Впервые за 28 лет депутатам придётся жить, лечиться, учить своих детей в условиях, которые они все эти годы создавали.', 'Интересно, а если провести обыск у всего руководства ФСБ - можно будет обратно понизить пенсионный возраст?', 'Позвонил друг из России, сказал, что берёт бутылку горилки, шмат сала и едет меня захватывать! Я сказал, что без боя не сдамся и купил ещё две бутылки водки и пару кило селёдки... Пусть тока сунется! А жинка моя ещё и ведро вареников налепила...)))', 'Лозунг "Задушим коррупцию" был признан экстремистским как призывающий к насильственному свержению существующего строя.', 'Находят митингующих по записям с видеокамер через нейросеть, хотя они в масках, их штрафуют, сажают… А вот человека, который выставил мою хату, спер дорогущий ноут, деньги, и лицо которого запечатлено на всех камерах подъезда, как-то блин, за два года найти не могут.']

info = '''
Игровой автомат 🎰
   Если вы получите 3 одинаковых смайлика(например 💎💎💎) получите 1₽
                        
Магазин🏦
    Тут вы можете закупиться разными предметами.
               
    Расслабляющий напиток🧉 с помощью него вы можете расслабиться от тяжёлой работы крутилщика слотов в НЕказино
              
    Допуск к колесу фортуны⭕️ теперь вы можете играть в колесо фортуны

    Мотивация💯 теперь вы можете ЗАМОТИВИРОВАТЬСЯ ИГРАТЬ В НЕКАЗИНО

    Анекдот. Вам грустно и нечем заняться, тогда купи анекдот и подними себе настроение!

    Статус Билл Гейтса. Вы самый богатый человек, владеете несколькими компаниями. Проще говоря вы прошли этого бота

    Капибара. Вы купили мотивацию и анекдот, но всё равно грустно и демотивированно. Тогда капибара для вас!Она поднимет и настроение, и мотивацию(100% гарантия)  

Колесо фортуны⭕️
    Если вам попадётся ⬛️ ваш баланс равняется 0, если 🟥 +10, 
    если 🟩 +100.Так что вы можеие и заработывать, и терять'''

async def info_handler(call: CallbackQuery, bot:Bot):
    await call.message.answer(eval(call.data), reply_markup=get_inline_keybords())

async def vibor(call: CallbackQuery, bot: Bot):
    score = store.get_score()
    await call.message.answer(text=f'{call.data} - ваш кошелёк-{score}₽', reply_markup=get_inline_keybords())
    await call.answer()

async def keybord_handler(call: CallbackQuery, bot: Bot):
    await call.message.answer("Добро пожаловать в магазин!",reply_markup=get_inline_keybords1()) 
    await call.answer()             

async def magazin_answer(call:CallbackQuery,callback_data:Product,answer:str):
    score = store.get_score()
    if score >= callback_data.price:
        await call.message.answer(text=answer, reply_markup=get_inline_keybords())
        store.change_score(-callback_data.price)
    else:
        await call.message.answer(text=f'Вам не хватает денег :(', reply_markup=get_inline_keybords())

async def magazin_handler(call: CallbackQuery, bot:Bot, callback_data:Product):
    if callback_data.name == 'Расслабляющий напиток':
        await magazin_answer(call,callback_data,'Поздравляю с покупкой!Теперь вы можете расслабиться!')
    if callback_data.name == 'Мотивация':
        await magazin_answer(call,callback_data,'Поздравляю с покупкой! Вот ваша мотивация: https://www.youtube.com/watch?v=RJQisT_dndc')
    if callback_data.name == 'Допуск к колесу фортуны':
        store.dopysk = True
        await magazin_answer(call,callback_data,'Поздравляю с покупкой! Теперь вы можете играть в колесо фортуны')
    if callback_data.name =='Статус Билл Гейтса':
        await magazin_answer(call,callback_data,'Поздравляю с покупкой!Теперь вы самый богатый человек в мире :)')
    if callback_data.name == 'Анекдот':
        random_game_for_one = choice(anekdot)
        await magazin_answer(call,callback_data,f'Поздравляю с покупкой!Вот тебе мой анекдот: {random_game_for_one}!')
    if callback_data.name == 'Капибара':
        await magazin_answer(call,callback_data,'Поздравляю с покупкой капибары', answer='data:image/jpeg;base64,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')
    call.answer()
    # score = store.get_score()
    # if score >= callback_data.price and callback_data.name == 'Расслабляющий напиток':
    #     await call.message.answer(text=f'Поздравляю с покупкой!Теперь вы можете расслабиться!')
    #     store.score = store.score - callback_data.price
    # if score < callback_data.price and callback_data.name == 'Расслабляющий напиток':
    #     await call.message.answer(text=f'Вам не хватает денег :(')

    # if score >= callback_data.price and callback_data.name == 'Мотивация':
    #     await call.message.answer(text=f'Поздравляю с покупкой! Вот ваша мотивация: https://www.youtube.com/watch?v=RJQisT_dndc')
    #     store.score = store.score - callback_data.price
    # if score < callback_data.price and callback_data.name == 'Мотивация':
    #     await call.message.answer(text=f'Вам не хватает денег :(')

    # if score >= callback_data.price and callback_data.name == 'Допуск к колесу фортуны':
    #     await call.message.answer(text=f'Поздравляю с покупкой! Теперь вы можете играть в колесо фортуны')
    #     store.score = store.score - callback_data.price
    #     store.dopysk = True
    # if score < callback_data.price and callback_data.name == 'Допуск к колесу фортуны':
    #     await call.message.answer(text=f'Вам не хватает денег :(')
