from aiogram import Bot, Dispatcher,F
import asyncio 
from handler import start_handler
from callback_handler import vibor,keybord_handler,magazin_handler,info_handler
from aiogram.filters import Command
from product import Product

TOKEN = '6405185096:AAGtWBpXUpPsooZVyFvsDzQbwtd4jzb2fd4'

async def start():

    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, Command(commands='start'))
    dp.callback_query.register(keybord_handler, F.data == 'Магазин')
    dp.callback_query.register(magazin_handler, Product.filter())
    dp.callback_query.register(info_handler, F.data == 'info')
    dp.callback_query.register(vibor)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start()) 
