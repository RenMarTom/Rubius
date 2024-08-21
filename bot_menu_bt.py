import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(token="7279092884:AAH3HxMAyUcs4PcEBSnmAzOO35r8e1tURgQ")

dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_buttons(message: types.Message):
    kb = [[types.KeyboardButton(text='Mashed potato'), types.KeyboardButton(text='Kholodets')],
          [types.KeyboardButton(text='Pasta')],
          [types.KeyboardButton(text='Soup'), types.KeyboardButton(text='Banana')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(text='What would you like to eat?', reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
