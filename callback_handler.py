from aiogram import Bot
from aiogram.types import CallbackQuery
from inline_keybords import get_inline_keybords, get_inline_keybords1
# from inline_keybords import koshelok
from store import store
from product import Product



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
