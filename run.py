import asyncio
import logging
import os
from dotenv import load_dotenv

load_dotenv()

from aiogram import Bot, Dispatcher, F
from app.handlers import router

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(BOT_TOKEN)
dp = Dispatcher()
photo1 = None



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit): 
        print("Bot stopped.")
