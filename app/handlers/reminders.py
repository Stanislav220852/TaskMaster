from aiogram import Router,F 
from aiogram.filters import Command
from aiogram.types import Message
from app.keyboards.keyboards import reminders_keyboard


reminder_router = Router()

@reminder_router.message(F.text == "⏰ Напоминания")
async def reminder(messege:Message):
    await messege.answer("Выбирите действие",reply_markup=reminders_keyboard)