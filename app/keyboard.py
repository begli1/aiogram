from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Catalog", callback_data='catalog')],
    [InlineKeyboardButton(text="Cart", callback_data='cart')],
    [InlineKeyboardButton(text="Contacts", callback_data='contacts')]
]
)


settings = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text="Youtube", url="https://youtube.com/")],
])

cars = ['Tesla', 'BMW', 'Mercedes', 'Audi']

async def get_cars_keyboard():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url="https://youtube.com/"))
    return keyboard.adjust(2).as_markup()