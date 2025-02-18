from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

resources = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт',url= 'https://cashonlyfun.com'),
     InlineKeyboardButton(text='Instagram*', url= 'https://www.instagram.com/cashonlyfun?igsh=MzRlODBiNWFlZA==')],
    [InlineKeyboardButton(text='Telegram канал', url = 'https://t.me/anycashonlyfun'),
     InlineKeyboardButton(text='Вконтакте', url= 'https://vk.com/anycashonlyfun')]
])