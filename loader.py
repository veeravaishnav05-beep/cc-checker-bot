from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
BOT_TOKEN = '7926504208:AAEw4m3q-7AQzAyDuUAkU62wVCsDIBcpUf4'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
