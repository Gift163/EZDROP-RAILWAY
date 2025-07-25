import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем переменные из .env (если ты локально тестируешь)
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("❌ BOT_TOKEN not found! Set it in Railway Variables or .env file.")
    exit()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        f"👋 Welcome to <b>EZDROP</b>!\n\n"
        "🎁 Open animated cases\n"
        "🖼️ Collect rare NFTs and $EZCOIN\n"
        "🌐 Powered by WebApp\n\n"
        "Tap below to start your journey 👇",
        parse_mode="HTML"
    )

    web_button = InlineKeyboardMarkup()
    web_button.add(InlineKeyboardButton("🌐 Launch EZDROP", web_app=WebAppInfo(url="https://ezdrop-rouge.vercel.app")))

    await message.answer("👇", reply_markup=web_button)

if __name__ == '__main__':
    executor.start_polling(dp)
