import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from inline_buttons import *
from buttons import *
dp = Dispatcher()
TOKEN = "6984778883:AAEF9MRStFHqIqT-Fo2vVv_EUzBMn3nR0UI"

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"""Assalomu Alaykum, {message.from_user.full_name} !\n\nIjodimizga qiziqish bildirganingiz uchun tashakkur!\n\nO'zbekiston bo'ylab yetkazib berish 2-5 ish kunini tashkil qiladi.\n\nToshkent bo'ylab yetkazib berish - 20 000 so'm.\n\nO‘zbekiston bo'ylab yetkazib berish - 30 000 so‘m.\n\n450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!\nAgar bu shartlar sizni qoniqtirsa, 🔥 Mahsulotlar bo'limiga o'tish orqali buyurtma berishni boshlashingiz mumkin.""", reply_markup=button)

@dp.message(F.text == "🔥 Mahsulotlar")
async def mahsulotlar(message: Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=button2)

@dp.message(F.text == "Phone")
async def phone(message: Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=product_btn_2)
    @dp.message(F.text == "Product 1")
    async def product_1(message: Message):
        await message.answer_photo(photo="https://www.creditasia.uz/upload/iblock/3d9/d8wxoqte183j0be3kf2ur3mdfs18pm6v/smartfon-apple-iphone-15-pro-max-256gb-blue-titanium.jpg", caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 2")
    async def product2(message: Message):
        await message.answer_photo(photo="https://www.creditasia.uz/upload/iblock/3d9/d8wxoqte183j0be3kf2ur3mdfs18pm6v/smartfon-apple-iphone-15-pro-max-256gb-blue-titanium.jpg", caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 3")
    async def product3(message: Message):
        await message.answer_photo(photo="https://www.creditasia.uz/upload/iblock/3d9/d8wxoqte183j0be3kf2ur3mdfs18pm6v/smartfon-apple-iphone-15-pro-max-256gb-blue-titanium.jpg", caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 4")
    async def product4(message: Message):
        await message.answer_photo(photo="https://www.creditasia.uz/upload/iblock/3d9/d8wxoqte183j0be3kf2ur3mdfs18pm6v/smartfon-apple-iphone-15-pro-max-256gb-blue-titanium.jpg", caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)


@dp.message(F.text == "Watch")
async def watch(message: Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=product_btn_3)

    @dp.message(F.text == "Product 1")
    async def product_1(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 2")
    async def product2(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 3")
    async def product3(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 4")
    async def product4(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)


@dp.message(F.text == "Laptop")
async def watch(message: Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=product_btn_4)

    @dp.message(F.text == "Product 1")
    async def product_1(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 2")
    async def product2(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 3")
    async def product3(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 4")
    async def product4(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)


@dp.message(F.text == "Keyboard")
async def keyboard(message: Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=product_btn_5)

    @dp.message(F.text == "Product 1")
    async def product_1(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 2")
    async def product2(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 3")
    async def product3(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)

    @dp.message(F.text == "Product 4")
    async def product4(message: Message):
        await message.answer_photo(
            photo="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MT613ref_VW_34FR+watch-49-titanium-ultra2_VW_34FR+watch-face-49-trail-ultra2_VW_34FR?wid=2000&hei=2000&fmt=png-alpha&.v=1694507270905",
            caption="iPhone 14 Pro\nApple IPhone 14 Pro Max, Deep Purple, 128 GB✔️\nApple: 100% Phone\nApple stikerlar to'plami futbolka bilan birga sovg'a sifatida jo'natiladi!\nProduct code: 54\nNarxi: 1500 USD", reply_markup=inline_btn)


@dp.message(F.text == "🏡 Bosh Menu")
async def menu(message: Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=button)


@dp.message(F.text == "👜 Hamkorlik")
async def hamkorlik(message: Message):
    await message.answer(f"Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz va sizning buyurtmangizga asosan futbolkalar, xudi, svitshot va boshqa ko'p narsalarni tayyorlashimiz mumkin.\nMenejer bilan bog'lanish uchun: @Musharraaf")




@dp.message(F.text == "ℹ️ Malumot")
async def malumot(message: Message):
    await message.answer("Kerakli bo'limni tanlang ⬇️", reply_markup=product_btn_6)



@dp.message(F.text == "🚀Yetkazib Berish Shartlari")
async def yetkazib_berish(message: Message):
    await message.answer("Yetkazib berish shartlari:\nO'zbekiston bo'ylab yetkazib berish 2-5 ish kuni ichida amalga oshiriladi.\nToshkent bo'ylab yetkazib berish - 20 USD.\nO‘zbekiston bo'ylab yetkazib berish - 30 USD.\n1 000 USD dan ortiq buyurtmalarni yetkazib berish - tekin!")


@dp.message(F.text == "alert")
async def alert(message: Message):
    await message.answer()

@dp.message(F.text == "☎️Kontaktlar")
async def contact(message: types.Message):
    a = "Mirfayoz"
    await message.answer_contact('+998993666674', first_name=a)



async def main()->None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
