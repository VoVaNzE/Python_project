from aiogram import Bot
from aiogram.types import Message
from inline_keybords import get_inline_keybords

async def start_handler(msg: Message, bot: Bot):
    await msg.answer("Салам! Я бот, где ты можешь получить зависимость к крутке слотов! Начинаем?",reply_markup=get_inline_keybords())
