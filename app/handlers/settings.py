from aiogram import Router,F 
from aiogram.filters import Command
from aiogram.types import Message
from app.keyboards.keyboards import settings_keyboard


settings_router = Router()

@settings_router.message(F.text == "⚙️ Настройки")
async def reminder(messege:Message):
    await messege.answer("Выбирите действие",reply_markup=settings_keyboard)