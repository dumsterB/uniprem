import os
import requests
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
    if splitted:
        for i in range(len(splitted)):
            if (splitted[i] == '_'):
                arr.append([splitted[i + 1], splitted[i + 2], splitted[i + 3], splitted[i + 4], splitted[i + 5], splitted[i + 6],splitted[i + 7], splitted[i + 8]])
        if arr:
            my_lst_str = ''.join(map(str, arr[0]))
            res = f'https://www.freepik.com/download-file/{my_lst_str}'
            await message.reply(res)
    # await bot.send_photo(message.chat.id,'')
    await message.reply_photo('https://imageio.forbes.com/specials-images/imageserve/5f962df3991e5636a2f68758/0x0.jpg?format=jpg&crop=812,457,x89,y103,safe&width=1200')


executor.start_polling(dp, skip_updates=True)
