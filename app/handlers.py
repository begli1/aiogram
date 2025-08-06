from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
import app.keyboard as kb

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Removing old keyboard...", reply_markup=ReplyKeyboardRemove())
    await message.reply(f'Hello, I am your bot!\nYour ID is {message.from_user.id}.\nYour full name is {message.from_user.full_name}',
                        reply_markup= await kb.get_cars_keyboard())

@router.message(Command('help'))
async def help_command(message: Message):
    await message.answer("Available commands:\n/start - Start the bot\n/help - Show this help message")

@router.message(F.text == "what's up" )
async def whats_up_command(message: Message):
    await message.answer("Not much, just hanging out! How about you?")

@router.message(F.photo)
async def photo_command(message: Message):
    global photo1
    photo1 = message.photo[-1].file_id
    await message.answer(f'ID Photo: {photo1}')

@router.message(Command('get_photo'))
async def get_photo_command(message: Message):
    await message.answer_photo(photo = photo1 , caption= "Here is the photo you sent!")