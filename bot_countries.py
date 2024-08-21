import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(token="7279092884:AAH3HxMAyUcs4PcEBSnmAzOO35r8e1tURgQ")

dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_buttons(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text='Russia', callback_data='c_rus')
    builder.button(text='Germany', callback_data='c_germ')
    builder.button(text='USA', callback_data='c_us')
    builder.button(text='Canada', callback_data='c_cnd')
    builder.button(text='Belgium', callback_data='c_blg')
    builder.adjust(3)

    await message.answer("Choose the country", reply_markup=builder.as_markup())


@dp.callback_query(F.data == 'c_rus')
async def cmd_start(callback: types.CallbackQuery):
    await callback.answer("Russia:\nPopulation: 145M\nPhone Code: +7", reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query(F.data == 'c_germ')
async def cmd_start(callback: types.CallbackQuery):
    await callback.answer("Germany:\nPopulation: 84M\nPhone Code: +49", reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query(F.data == 'c_us')
async def cmd_start(callback: types.CallbackQuery):
    await callback.answer("USA:\nPopulation: 330M\nPhone Code: +1", reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query(F.data == 'c_cnd')
async def cmd_start(callback: types.CallbackQuery):
    await callback.answer("Canada:\nPopulation: 39M\nPhone Code: +1", reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query(F.data == 'c_blg')
async def cmd_start(callback: types.CallbackQuery):
    await callback.answer("Belgium:\nPopulation: 12M\nPhone Code: +32", reply_markup=types.ReplyKeyboardRemove())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
