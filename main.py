import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from datetime import datetime


from src.app.handlers.user import user_router
from src.app.handlers.catalog import catalog_router
#from src.app.handlers.admin import admin_router
from src.database.models import async_main

import sys
sys.path.append('../photo')

load_dotenv()

TOKEN = os.getenv("TOKEN")
#EVENING_CHAT_ID = os.getenv("EVENING_CHAT_ID")
#ADMIN_TG_ID = os.getenv("ADMIN_TG_ID")


async def on_startup(dispatcher: Dispatcher):
    await async_main()


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(user_router, catalog_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down")
