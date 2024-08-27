import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

a = 0
b = 0
c = ''
d = 0

bot = Bot(token="7257452276:AAFK0xdo4Z-HWAG-0LJTXErXNAFib76qhEk")

dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_buttons(message: types.Message):
    global a, b
    kb = [[types.KeyboardButton(text='+'), types.KeyboardButton(text='-')],
          [types.KeyboardButton(text='*'),
           types.KeyboardButton(text='/')], [types.KeyboardButton(text='^')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(text='working...', reply_markup=keyboard)
    a = 0
    b = 0


@dp.message(Command('equal'))
async def cmd_buttons(message: types.Message):
    global a
    await message.answer(str(a))


@dp.message(Command('exit'))
async def cmd_buttons(message: types.Message):
    await message.answer('finish!', reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text == '+')
async def cmd_buttons(message: types.Message):
    global c
    c = '+'


@dp.message(F.text == '-')
async def cmd_buttons(message: types.Message):
    global c
    c = '-'


@dp.message(F.text == '*')
async def cmd_buttons(message: types.Message):
    global c
    c = '*'


@dp.message(F.text == '/')
async def cmd_buttons(message: types.Message):
    global c
    c = '/'


@dp.message(F.text == '^')
async def cmd_buttons(message: types.Message):
    global c
    c = '**'


@dp.message(F.text)
async def cmd_buttons(message: types.Message):
    global a, b, c, d
    if d != 0:
        b = int(message.text)
        if c == '+':
            a = a + b
            await message.answer(text=str(a))
        if c == '-':
            a = a - b
            await message.answer(text=str(a))
        if c == '*':
            a = a * b
            await message.answer(text=str(a))
        if c == '/':
            a = a / b
            await message.answer(text=str(a))
        if c == '**':
            a = a ** b
            await message.answer(text=str(a))
    else:
        a = int(message.text)
        d = 1


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
