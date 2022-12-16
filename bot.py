import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN='5879394130:AAGw9NgBEpycnISeNDfUP5VF_sYjf11UUYQ'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    link = message.text
    splitted = [*link]
    arr = []
    # get the id of the picture
    for i in range(len(splitted)):
        if (splitted[i] == '_'):
            arr.append([splitted[i + 1], splitted[i + 2], splitted[i + 3], splitted[i + 4], splitted[i + 5], splitted[i + 6],splitted[i + 7], splitted[i + 8]])
    my_lst_str = ''.join(map(str, arr[0]))
    res = f'https://www.freepik.com/download-file/{my_lst_str}'
    await message.reply(res)


executor.start_polling(dp, skip_updates=True)
