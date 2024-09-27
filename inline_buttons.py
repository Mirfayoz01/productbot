from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Batafsil", callback_data="alert")], # noqa
    [InlineKeyboardButton(text="Buyurtma Berish", callback_data="buyurtma", url="https://t.me/MYSTERIOUS_06"), ] # noqa
]) # noqa