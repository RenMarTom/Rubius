import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(token="7279092884:AAH3HxMAyUcs4PcEBSnmAzOO35r8e1tURgQ")

dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_buttons(message: types.Message):
    kb = [[types.KeyboardButton(text='To the forest'),
           types.KeyboardButton(text='To the river'),
           types.KeyboardButton(text='Home')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('You entered the forest. Where will you go next?', reply_markup=keyboard)


@dp.message(F.text == 'Home')
async def cmd_start(message=types.Message):
    await message.answer("You've came back home", reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text == 'To the river')
async def cmd_start(message: types.Message):
    kb = [[types.KeyboardButton(text='Go swimming'),
           types.KeyboardButton(text='Go fishing')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("You've came to the river. What will you do next?", reply_markup=keyboard)


@dp.message(F.text == 'Go swimming')
async def cmd_start(message=types.Message):
    await message.answer("You've cool down and went back home", reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text == 'Go fishing')
async def cmd_start(message=types.Message):
    await message.answer("You've caught fish and went back home", reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text == 'To the forest')
async def cmd_start(message: types.Message):
    kb = [[types.KeyboardButton(text="Pretend like you're died"),
           types.KeyboardButton(text='Go back quietly')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("You've met the bear. What will you do next?", reply_markup=keyboard)


@dp.message(F.text == "Pretend like you're died")
async def cmd_start(message=types.Message):
    await message.answer("The bear has left this place", reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text == 'Go back quietly')
async def cmd_start(message=types.Message):
    await message.answer("You've quietly go back home", reply_markup=types.ReplyKeyboardRemove())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
