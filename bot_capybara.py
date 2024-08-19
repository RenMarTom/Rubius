from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import time
import asyncio

bot = Bot(token='7279092884:AAH3HxMAyUcs4PcEBSnmAzOO35r8e1tURgQ')
dp = Dispatcher()


@dp.message(Command("капи"))
async def cmd_text(message: types.Message):
    msg = await message.answer_photo(types.FSInputFile("C:/Users/englishteacher/Desktop/Капибары/1.jpg"))
    time.sleep(2)
    await msg.delete()
    msg = await message.answer_photo(types.FSInputFile("C:/Users/englishteacher/Desktop/Капибары/3.webp"))
    time.sleep(2)
    await msg.delete()
    msg = await message.answer_photo(types.FSInputFile("C:/Users/englishteacher/Desktop/Капибары/4.jpg"))
    time.sleep(2)
    await msg.delete()
    msg = await message.answer_photo(types.FSInputFile("C:/Users/englishteacher/Desktop/Капибары/5.jpg"))
    time.sleep(2)
    await msg.delete()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
