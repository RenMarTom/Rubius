import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

bot = Bot(token="7257452276:AAFK0xdo4Z-HWAG-0LJTXErXNAFib76qhEk")

dp = Dispatcher()

dict = {}


@dp.message(Command('start'))
async def cmd_buttons(message: types.Message):
    kb = [[types.KeyboardButton(text='+'), types.KeyboardButton(text='-')],
          [types.KeyboardButton(text='*'),
           types.KeyboardButton(text='/')], [types.KeyboardButton(text='^')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    un = message.from_user.username
    dict[un] = [0, 0, '', 0]
    await message.answer(text='working...', reply_markup=keyboard)
    dict[un][0] = 0
    dict[un][1] = 0


@dp.message(Command('equal'))
async def cmd_buttons(message: types.Message):
    un = message.from_user.username
    await message.answer(str(dict[un][0]))


@dp.message(Command('exit'))
async def cmd_buttons(message: types.Message):
    await message.answer('finish!', reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text == '+')
async def cmd_buttons(message: types.Message):
    un = message.from_user.username
    dict[un][2] = '+'


@dp.message(F.text == '-')
async def cmd_buttons(message: types.Message):
    un = message.from_user.username
    dict[un][2] = '-'


@dp.message(F.text == '*')
async def cmd_buttons(message: types.Message):
    un = message.from_user.username
    dict[un][2] = '*'


@dp.message(F.text == '/')
async def cmd_buttons(message: types.Message):
    un = message.from_user.username
    dict[un][2] = '/'


@dp.message(F.text == '^')
async def cmd_buttons(message: types.Message):
    un = message.from_user.username
    dict[un][2] = '**'


@dp.message(F.text)
async def cmd_buttons(message: types.Message):
    un = message.from_user.username
    if dict[un][3] != 0:
        dict[un][1] = int(message.text)
        if dict[un][2] == '+':
            dict[un][0] = dict[un][0] + dict[un][1]
            await message.answer(text=str(dict[un][0]))
        if dict[un][2] == '-':
            dict[un][0] = dict[un][0] - dict[un][1]
            await message.answer(text=str(dict[un][0]))
        if dict[un][2] == '*':
            dict[un][0] = dict[un][0] * dict[un][1]
            await message.answer(text=str(dict[un][0]))
        if dict[un][2] == '/':
            dict[un][0] = dict[un][0] / dict[un][1]
            await message.answer(text=str(dict[un][0]))
        if dict[un][2] == '**':
            dict[un][0] = dict[un][0] ** dict[un][1]
            await message.answer(text=str(dict[un][0]))
    else:
        dict[un][0] = int(message.text)
        dict[un][3] = 1


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
