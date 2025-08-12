from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from app.requests import get_categories , get_items_by_category
main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Catalog", callback_data='catalog')],
    [InlineKeyboardButton(text="Cart", callback_data='cart')],
    [InlineKeyboardButton(text="Contacts", callback_data='contacts')]
], resize_keyboard=True,
    input_field_placeholder="Choose an option"
)

async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text="Back to main menu", callback_data='main_menu'))
    return keyboard.adjust(1).as_markup()






async def items(category_id):
    all_items = await get_items_by_category(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
    keyboard.add(InlineKeyboardButton(text="Back to main menu", callback_data='main_menu'))
    return keyboard.adjust(1).as_markup()

async def back_to_main_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Back to main menu", callback_data='main_menu'))
    return keyboard.adjust(1).as_markup()