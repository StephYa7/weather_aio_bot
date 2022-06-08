import logging
from aiogram import types, Bot, Dispatcher, executor
import requests

logging.basicConfig(level=logging.INFO)
bot = Bot(token='5366132013:AAGE6UIyaydlwThANfwQuy64ZgG9AReVKAM')
dp = Dispatcher(bot)
weather_tok = '16810cda7329a6f0815f5598e348c911'


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("/weather погода")

@dp.message_handler(commands=['weather'])
async def get_weath(message: types.Message):
    await message.reply('Введите город:')

    @dp.message_handler()
    async def city(message: types.Message):
        coord = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={message.text}&appid={weather_tok}')
        data_coord = coord.json()
        lat = data_coord[0]['lat']
        lon = data_coord[0]['lon']
        ci = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_tok}&units=metric&lang=ru')
        data = ci.json()
        city = data['name']
        temp = data['main']['temp']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        
        await message.reply(f'Погода в {city}:\nТемпература: {temp}\nДавление: {pressure}\nСкорость ветра: {wind}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)