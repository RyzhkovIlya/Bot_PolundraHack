import os
import logging
import time

from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from api.model import picture
from api.utils.static import START, INFO

# Логирование
logging.basicConfig(filename='log.log',
                    # encoding='utf-8',
                    level=logging.INFO)

# Загрузка токена через env
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    logging.info(f'{user_id} запустил бота в {time.asctime()}')
    await message.reply(START % user_name, parse_mode='Markdown')


@dp.message_handler(commands=['info'])
async def process_help_command(message: types.Message):
    await message.reply(INFO)


@dp.message_handler()
async def echo_message(message: types.Message):
    txt = message.text
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if message.content_type != 'text':
        await bot.send_message(user_id, 'Пришлите текст - одно слово, другие типы данных не поддерживаются')
    elif not txt.isalpha():
        await bot.send_message(user_id, 'Пришлите одно слово, без цифр и специальных символов')
    elif len(txt) > 15:
        await bot.send_message(user_id, 'Пришлите одно слово длиной не более 10 символов')
    else:
        logging.info(f'Нам написал {user_name}, его id = {user_id}')
        await bot.send_message(user_id, picture(txt))


if __name__ == '__main__':
    executor.start_polling(dp)
