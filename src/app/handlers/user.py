from datetime import datetime

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery

import src.app.keyboards.start_keyboard as s_kb
import src.app.keyboards.catalog_keyboard as c_kb
import src.app.keyboards.resources_keyboard as r_kb

from src.database.requests import (set_user, get_user)


user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id, message.from_user.username)
    user = await get_user(message.from_user.id)
    request_user_name = user.user_full_name if user.user_full_name is not None else user.tg_name
    await message.answer(f"Добро пожаловать в наш магазин, {request_user_name} !",
                         reply_markup=s_kb.main)

# @user_router.message(F.text == 'Мои заказы')
# async def my_orders(message: Message):
#     await message.answer('Список заказов пуст')

@user_router.message(F.text == 'Каталог товаров')
async def catalog(message: Message):
    await message.answer('Выберите категорию',
                         reply_markup=c_kb.catalog)

# @user_router.message(F.text == 'Доставка')
# async def delivery(message: Message):
#     await message.answer('')

# @user_router.message(F.text == 'FAQ')
# async def faq(message: Message):
#     await message.answer('')

@user_router.message(F.text == 'Наши ресурсы')
async def resources(message: Message):
    await message.answer('Наши ресурсы\n*Признан экстремистской организацией и запрещен на территории РФ.',
                         reply_markup=r_kb.resources)