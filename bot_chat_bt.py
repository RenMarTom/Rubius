import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(token="7279092884:AAH3HxMAyUcs4PcEBSnmAzOO35r8e1tURgQ")

dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_buttons(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text='-2', callback_data='-2')
    builder.button(text='-1', callback_data='-1')
    builder.button(text='1', callback_data='1')
    builder.button(text='2', callback_data='2')
    builder.button(text='Confirm', callback_data='random_text')
    builder.adjust(4)

    builder.row(types.InlineKeyboardButton(text='Hello', callback_data='Hello'),
                types.InlineKeyboardButton(text='Bye', callback_data='Bye'),
                width=2)

    await message.answer("Push the button", reply_markup=builder.as_markup())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
