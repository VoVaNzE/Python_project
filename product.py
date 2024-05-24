from aiogram.filters.callback_data import CallbackData

class Product(CallbackData, prefix='low'):
    name:str
    price:int
