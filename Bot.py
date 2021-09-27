import os
import logging

import time
from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from api.utils.static import START, INFO
from google_images_search import GoogleImagesSearch

from api.model import picture
# from api.utils.config import TOKEN

#включаем логирование
logging.basicConfig(filename='log.log',
                     encoding='utf-8',
                     level=logging.INFO)

load_dotenv()
TOKEN=os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_name = message.from_user.first_name
    logging.info((f'{user_name} написал нам в {time.asctime()}'))
    await message.reply(START %user_name, parse_mode='MarkdownV2')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(INFO)


@dp.message_handler()
async def echo_message(message: types.Message):
    type = message.content_type
    if message.text.isalpha() and len(message.text) <= 10:
        user_name = message.from_user.first_name
        user_id = message.from_user.id
        logging.info(f'Нам написал {user_name}, его id = {user_id}')
        await bot.send_photo(user_id, picture(message.text))
    else:
        user_name = message.from_user.first_name
        user_id = message.from_user.id
        logging.info(f'Нам написал {user_name}, его id = {user_id}')
        await bot.send_message(message.from_user.id, f'{type} формат не поддерживается, друг, попробуй еще раз, введи одно слово длинной не более 10 символов, ты ввел {len(message.text)} символов')
    # await bot.send_message(message.from_user.id, squar(int(message.text)))

if __name__ == '__main__':
    executor.start_polling(dp)