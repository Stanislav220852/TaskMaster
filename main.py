import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from app.core.config import settings
from app.keyboards.keyboards import main_kb
from app.handlers.tasks import tasks_router
from app.handlers.reminders import reminder_router
from app.handlers.settings import settings_router

from app.user.services.user_services import UserServices

bot = Bot(token = settings.BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_bot(messege:Message):
    user = await UserServices.add_user(telegram_id=messege.from_user.id,language=messege.from_user.language_code or "ru")

    await messege.answer(f'Hello {messege.from_user.first_name}',reply_markup=main_kb)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(tasks_router)
    dp.include_router(reminder_router)
    dp.include_router(settings_router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
