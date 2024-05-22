from aiogram import Bot
from aiogram.types import CallbackQuery
from inline_keybords import get_inline_keybords
from inline_keybords import koshelok

async def vibor(call: CallbackQuery, bot: Bot):
    await call.message.answer(text=f'{call.data}- ваш кошелёк-{koshelok}₽', reply_markup=get_inline_keybords())
    await call.answer                           
