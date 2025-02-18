from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Мои заказы'),
     KeyboardButton(text='Каталог товаров')],
    [KeyboardButton(text='Доставка'),
     KeyboardButton(text='FAQ')],
    [KeyboardButton(text='Корзина'),
     KeyboardButton(text='Наши ресурсы')]
],
    resize_keyboard= True,
    input_field_placeholder='Выберите пункт ниже')