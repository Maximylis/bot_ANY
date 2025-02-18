from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

t_shirt_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back'),
     InlineKeyboardButton(text='1 из 12', callback_data='none'),
     InlineKeyboardButton(text='Вперед', callback_data='next')],
    [InlineKeyboardButton(text='Каталог', callback_data='in_catalog'),
     InlineKeyboardButton(text='В корзину', callback_data='in_basket')]
])