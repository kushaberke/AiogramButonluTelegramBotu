from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

bot = Bot(token="6131046247:AAHtEClT_cXFg2LXRK1IZrL1btNebDJxVPU")

dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="Excel",url="https://www.youtube.com/watch?v=SP6wt6sRPkg")
button2 = InlineKeyboardButton(text="Metin",callback_data="metinver")
button3 = InlineKeyboardButton(text="Sayı",callback_data="sayiver")

keyboard1 = InlineKeyboardMarkup().add(button1).add(button2).add(button3)

@dp.callback_query_handler(text = ["metinver","sayiver"])

async def metin(call:types.CallbackQuery):
    if call.data =="metinver":
        await call.message.answer("Kusha Mühendislik")
    if call.data == "sayiver":
        await call.message.answer("15")
    await call.answer()

@dp.message_handler(commands=['start','help'])

async def basla(message:types.Message):
    await message.reply("Hello",reply_markup=keyboard1)


@dp.message_handler()

async def echo(message:types.Message):
    await message.answer(message.text)


executor.start_polling(dp)