from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, FSInputFile
import os

import src.app.keyboards.t_shirts_keyboard as t_kb

DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__)) + '/photo'

catalog_router = Router()

@catalog_router.callback_query(F.data == 't-shirts')
async def t_shirt_1(callback: CallbackQuery):

    # photo_1 = InputMediaPhoto(type='photo',
    #                           media=FSInputFile(path=DIRECTORY_PATH + '/t_shirts/A110/A110_1.JPG'))
    photo_2 = InputMediaPhoto(type='photo',
                              media=FSInputFile(path=DIRECTORY_PATH + '/t_shirts/A110/A110_2.JPG'))
    photo_3 = InputMediaPhoto(type='photo',
                              media=FSInputFile(path=DIRECTORY_PATH + '/t_shirts/A110/A110_3.JPG'))
    photo_4 = InputMediaPhoto(type='photo',
                              media=FSInputFile(path=DIRECTORY_PATH + '/t_shirts/A110/A110_4.JPG'))

    media = [photo_2, photo_3, photo_4]

    await callback.answer(' ')
    await callback.message.answer('Футболка черная ANY Cash, only fun Black\n'
                         'Артикул А110\n'
                         'Размер: One Size\n'
                         '\n'
                         'Описание:\n'
                         '\n'
                         'Стильная черная футболка из нежного хлопка станет идеальным дополнением вашего гардероба. '
                         'Элегантный крой обеспечивает комфорт и свободу движений, а яркая красная вышивка с названием '
                         'бренда «Any Cash, only fun» придаёт футболке уникальность и яркость. Подходит как для '
                         'повседневной носки, так и для создания стильных нарядов.'
                         '\n'
                         'Сделано в России.\n'
                         '\n'
                         'Цена: 8.000 рублей.'
)
    await callback.message.answer_media_group(media)
    await callback.message.answer(text='Выберите действие', reply_markup=t_kb.t_shirt_1)
