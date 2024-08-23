import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

money = 5000
cars = 0

bot = Bot(token="7279092884:AAH3HxMAyUcs4PcEBSnmAzOO35r8e1tURgQ") #bot name: @MRubius_bot

dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_buttons(message: types.Message):
    kb = [[types.KeyboardButton(text='Go to the car showroom'),
           types.KeyboardButton(text='Go and work'),
           types.KeyboardButton(text='Go home')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("You've finished the school, now you have 5'000$. What do you want to do now?",
                         reply_markup=keyboard)


@dp.message(F.text == 'Go home')
async def cmd_start(message=types.Message):
    global money
    global cars
    kb = [[types.KeyboardButton(text='Go to the car showroom'),
           types.KeyboardButton(text='Go and work'),
           types.KeyboardButton(text='Go home')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"You've came back home, you've got {money}$ and {cars} cars", reply_markup=keyboard)


@dp.message(F.text == 'Go to the car showroom')
async def cmd_start(message: types.Message):
    global money
    kb = [[types.KeyboardButton(text="Cheap car (10'000$)"),
           types.KeyboardButton(text="Middle-class car (25'000$)"),
           types.KeyboardButton(text="Luxury car (75'000$)")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"You've came to the car showroom. You have {money}$ Which car would you like to buy?",
                         reply_markup=keyboard)


@dp.message(F.text == "Cheap car (10'000$)")
async def cmd_start(message=types.Message):
    global money
    kb = [[types.KeyboardButton(text='Go to the car showroom'),
           types.KeyboardButton(text='Go and work'),
           types.KeyboardButton(text='Go home')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    if money >= 10000:
        global cars
        cars += 1
        money -= 10000
        await message.answer("Now you have a car! Congrats!", reply_markup=keyboard)
    else:
        await message.answer("You haven't got enough money! You have to work!", reply_markup=keyboard)


@dp.message(F.text == "Middle-class car (25'000$)")
async def cmd_start(message=types.Message):
    global money
    kb = [[types.KeyboardButton(text='Go to the car showroom'),
           types.KeyboardButton(text='Go and work'),
           types.KeyboardButton(text='Go home')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    if money >= 25000:
        await message.answer("Now you have a car! Congrats!", reply_markup=keyboard)
        global cars
        cars += 1
        money -= 25000
    else:
        await message.answer("You haven't got enough money! You have to work!", reply_markup=keyboard)


@dp.message(F.text == "Luxury car (75'000$)")
async def cmd_start(message=types.Message):
    global money
    kb = [[types.KeyboardButton(text='Go to the car showroom'),
           types.KeyboardButton(text='Go and work'),
           types.KeyboardButton(text='Go home')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    if money >= 75000:
        await message.answer("Now you have a car! Congrats!", reply_markup=keyboard)
        global cars
        cars += 1
        money -= 75000
    else:
        await message.answer("You haven't got enough money! You have to work!", reply_markup=keyboard)


@dp.message(F.text == "Go and work")
async def cmd_start(message=types.Message):
    global money
    money += 10000
    kb = [[types.KeyboardButton(text='Go to the car showroom'),
           types.KeyboardButton(text='Go and work'),
           types.KeyboardButton(text='Go home')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("You've earned 10'000$", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
