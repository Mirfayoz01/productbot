from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

buttons = [
    [KeyboardButton(text="🔥 Mahsulotlar"), KeyboardButton(text="ℹ️ Malumot")],
    [KeyboardButton(text="👜 Hamkorlik")]
]
button = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

tovar_btn = [
    [KeyboardButton(text="Phone"), KeyboardButton(text="Watch")],
    [KeyboardButton(text="Laptop"), KeyboardButton(text="Keyboard")],
    [KeyboardButton(text="🏡 Bosh Menu")]
]
button2 = ReplyKeyboardMarkup(keyboard=tovar_btn, resize_keyboard=True)
product_btn = [
    [KeyboardButton(text="Product 1"), KeyboardButton(text="Product 2")],
    [KeyboardButton(text="Product 3"), KeyboardButton(text="Product 4")],
    [KeyboardButton(text="🏡 Bosh Menu")]
]
product_btn_2 = ReplyKeyboardMarkup(keyboard=product_btn, resize_keyboard=True)

product_btn2 = [
    [KeyboardButton(text="Product 1"), KeyboardButton(text="Product 2")],
    [KeyboardButton(text="Product 3"), KeyboardButton(text="Product 4")],
    [KeyboardButton(text="🏡 Bosh Menu")]
]
product_btn_3 = ReplyKeyboardMarkup(keyboard=product_btn2, resize_keyboard=True)

product_btn3 = [
    [KeyboardButton(text="Product 1"), KeyboardButton(text="Product 2")],
    [KeyboardButton(text="Product 3"), KeyboardButton(text="Product 4")],
    [KeyboardButton(text="🏡 Bosh Menu")]
]
product_btn_4 = ReplyKeyboardMarkup(keyboard=product_btn3, resize_keyboard=True)

product_btn4 = [
    [KeyboardButton(text="Product 1"), KeyboardButton(text="Product 2")],
    [KeyboardButton(text="Product 3"), KeyboardButton(text="Product 4")],
    [KeyboardButton(text="🏡 Bosh Menu")]
]
product_btn_5 = ReplyKeyboardMarkup(keyboard=product_btn4, resize_keyboard=True)

product_btn5 = [
    [KeyboardButton(text="✍️Izoh Qoldirish")],
    [KeyboardButton(text="🚀Yetkazib Berish Shartlari"), KeyboardButton(text="☎️Kontaktlar")],
    [KeyboardButton(text="🏡 Bosh Menu")]
]
product_btn_6 = ReplyKeyboardMarkup(keyboard=product_btn5, resize_keyboard=True)