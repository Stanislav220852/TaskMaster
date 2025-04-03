from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command
from app.keyboards.keyboards import task_keyboard, filter_keyboard,main_kb



tasks_router = Router()


@tasks_router.message(F.text == "📝 Добавить задачу")
async def add_task(messege:Message):
    await messege.answer("Выберите действие",reply_markup=task_keyboard)

@tasks_router.message(F.text == "📋 Список задач")
async def get_task(messege:Message):
    await messege.answer("Выберите действие",reply_markup=filter_keyboard)

@tasks_router.message(F.text == "◀️ Назад")
async def back(messege:Message):
    await messege.answer("Выберите действие",reply_markup=main_kb)