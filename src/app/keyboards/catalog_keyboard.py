from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Футболки', callback_data='t-shirts'),
     InlineKeyboardButton(text='Платья', callback_data='dresses')],
    [InlineKeyboardButton(text='Свитшоты', callback_data='sweatshirts'),
     InlineKeyboardButton(text='Купальники', callback_data='swimwear')],
    [InlineKeyboardButton(text='Штаны', callback_data='pants'),
     InlineKeyboardButton(text='Шубы', callback_data='fur_coats')]
])