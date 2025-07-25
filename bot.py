from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, InputFile
from aiogram.utils import executor
import logging
import os
from dotenv import load_dotenv

# Загрузка токена
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Путь к изображению (можешь заменить на своё)
IMAGE_PATH = "ezdrop_preview.jpg"  # загрузи файл с таким именем в репозиторий

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    photo = InputFile(IMAGE_PATH)

    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton("🚀 Open EZDROP", web_app=WebAppInfo(url="https://ezdrop-rouge.vercel.app"))
    )

    await message.answer_photo(
        photo=photo,
        caption=(
            "👋 Welcome to *EZDROP*!\n\n"
            "Unbox unique NFTs, earn rewards, and explore exclusive cases inside our WebApp.\n\n"
            "Click the button below to start your journey 👇"
        ),
        reply_markup=markup,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
