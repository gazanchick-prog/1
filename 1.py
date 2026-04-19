import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN_1 = '8706163577:AAEmPvM7S_GCPPR2_AgLJx4BV00lbk1dLLA'
bot = Bot(token=TOKEN_1)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⭐ Получить 50 звёзд", callback_data="gift_stars")],
        [InlineKeyboardButton(text="🖼 Получить NFT", callback_data="gift_nft")]
    ])
    await message.answer("Выберите свой подарок:", reply_markup=kb)

@dp.callback_query(F.data.in_(["gift_stars", "gift_nft"]))
async def task(call: types.CallbackQuery):
    count = 40 if call.data == "gift_stars" else 60
    text = (f"Чтобы забрать награду, выполните задание:\n\n"
            f"Разошлите в ТТ текст: \"@zyozp дарит подарки\" {count} раз.\n"
            f"После этого отправьте скриншоты админу и переходите в бота для получения:\n"
            f"👉 https://t.me/Zyozpstarbot") # ЗАМЕНИ НА ЮЗЕРНЕЙМ ВТОРОГО БОТА
    await call.message.edit_text(text)

if __name__ == '__main__':
    dp.run_polling(bot)
