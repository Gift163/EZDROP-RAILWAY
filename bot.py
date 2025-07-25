import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем токен из .env (если ты используешь .env)
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверка на наличие токена
if not BOT_TOKEN:
    print("❌ BOT_TOKEN not found. Please set it in .env or Railway variables.")
    exit()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    name = message.from_user.first_name

    text = (
        f"👋 Welcome, <b>{name}</b>!\n\n"
        "You're now in <b>EZDROP</b> — a next-gen Telegram game where:\n\n"
        "🎁 Open animated cases and win rewards\n"
        "🖼️ Collect exclusive NFTs and $EZCOIN tokens\n"
        "🌐 All connected to a full-featured WebApp\n\n"
        "Start your journey now 👇"
    )

    await message.answer(text, parse_mode="HTML")

    web_kb = InlineKeyboardMarkup()
    web_kb.add(InlineKeyboardButton("🌐 Launch EZDROP WebApp", web_app=WebAppInfo(url="https://ezdrop-rouge.vercel.app")))

    await message.answer("Tap below to start:", reply_markup=web_kb)

if name == '__main__':
    executor.start_polling(dp)
