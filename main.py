from aiogram import Bot, Dispatcher
import asyncio 
from handler import start_handler
from callback_handler import vibor
from aiogram.filters import Command

TOKEN = '7187758450:AAHiCMAuAVH4GYD6CkKb8wDj_lEjT5MM3F0'

async def start():

    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, Command(commands='start'))
    dp.callback_query.register(vibor)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start()) 