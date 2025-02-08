from datetime import datetime

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery

# import src.app.keyboards.kb as kb
from src.database.requests import (set_user, get_user)


user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id, message.from_user.username)
    user = await get_user(message.from_user.id)
    request_user_name = user.user_full_name if user.user_full_name is not None else user.tg_name
    await message.answer(f"Привет {request_user_name} !")