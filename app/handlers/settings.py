from aiogram import Router,F 
from aiogram.filters import Command
from aiogram.types import Message
from app.keyboards.keyboards import settings_keyboard, language_keyboard


settings_router = Router()

@settings_router.message(F.text == "⚙️ Настройки")
async def reminder(messege:Message):
    await messege.answer("Выберите действие",reply_markup=settings_keyboard)

@settings_router.message(F.text == "🌍 Язык")
async def language_settings(messege:Message):
    await messege.answer("Выберите язык",reply_markup=language_keyboard)