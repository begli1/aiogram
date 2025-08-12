import asyncio
import logging
import os
from dotenv import load_dotenv

load_dotenv()

from aiogram import Bot, Dispatcher, F
from app.handlers import router
from app.models import async_main


BOT_TOKEN = os.getenv("TOKEN")




async def main():
    await async_main()
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit): 
        print("Bot stopped.")
