from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboard as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.middleware import TestMiddleWare
import app.requests as rq
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()



class Reg(StatesGroup):
    name = State()
    number = State()

router.message.middleware(TestMiddleWare())

@router.message(CommandStart())
async def start_command(message: Message):
    await message.reply(f'Welcome to the sneaker store!',
                        reply_markup= kb.main) #await cannot be used here as it is not an async function



@router.callback_query(F.data == "main_menu")
async def main_menu(callback: CallbackQuery):
    await callback.message.reply(f'Welcome to the sneaker store!',
                                  reply_markup= kb.main)

@router.callback_query(F.data == "catalog")
async def catalog_command(callback: CallbackQuery):
    await callback.message.answer("This is the catalog", reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category_callback(callback: CallbackQuery):
    await callback.answer("You selected a category")
    await callback.message.answer("Here are the items in this category:", reply_markup=await kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def item_callback(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer("You selected an item")
    await callback.message.answer(f'Name: {item_data.name}\nDescription: {item_data.description}\nPrice: {item_data.price}', reply_markup=await kb.back_to_main_menu())