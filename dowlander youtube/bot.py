from pytube import YouTube
import aiogram
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
import asyncio
import logging
import sys
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.types import CallbackQuery
TOKEN = "6632943217:AAFFo8SRjTxfvSq2_fjY9N4z0ufnnc3et1E"

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message:Message):
    await message.answer(text="Assalomu alaykum! YouTube videoning URLini tashlang!")


from aiogram.types import FSInputFile
@dp.message(F.text)
async def answer_obhavo(message: Message):
    try:
        yt = YouTube(message.text)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        video = FSInputFile(f"{yt.title}.mp4")
        await message.answer_video(video=video)

    except:
        await message.answer(text="Afsuski, bu videoni tashlab olib bo'lmaydi! Iltimos boshqa videoning URLini tashlang!")

async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)





if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

