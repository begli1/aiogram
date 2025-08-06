import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from config import TOKEN
from app.handlers import router


bot = Bot(TOKEN)
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
