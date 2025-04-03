from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


main_kb = ReplyKeyboardMarkup(keyboard=[
    
    [
        KeyboardButton(text="📝 Добавить задачу"),
        KeyboardButton(text="📋 Список задач"),
    ],
        
    [
        KeyboardButton(text="⏰ Напоминания"),
        KeyboardButton(text="⚙️ Настройки"),
    ],
],resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Выберите действие из меню",selective=True
)


task_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сегодня"),
            KeyboardButton(text="Завтра"),
        ],
        [
            KeyboardButton(text="Через час"),
            KeyboardButton(text="Выбрать дату"),
        ],
        [
            KeyboardButton(text="◀️ Назад"),
        ],
    ],
    resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Выберите действие из меню",selective=True
)

filter_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔢 По дате"),
            KeyboardButton(text="🏷️ По категории"),
        ],
        [
            KeyboardButton(text="✅ Выполненные"),
            KeyboardButton(text="❌ Невыполненные"),
        ],
        [
            KeyboardButton(text="◀️ Назад"),
        ],
    ],
    resize_keyboard=True
)

settings_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌍 Язык"),
            KeyboardButton(text="🔔 Уведомления"),
        ],
        [
            KeyboardButton(text="📅 Google Calendar"),
            KeyboardButton(text="◀️ Назад"),
        ],
    ],
    resize_keyboard=True
)

language_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇷🇺 Русский"),
            KeyboardButton(text="🇬🇧 English"),
        ],
        [
            KeyboardButton(text="◀️ Назад"),
        ],
    ],
    resize_keyboard=True
)

reminders_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏳ Разовое напоминание"),
            KeyboardButton(text="🔄 Повторяющееся"),
        ],
        [
            KeyboardButton(text="🚀 Быстрый выбор"),
            KeyboardButton(text="📋 Мои напоминания"),
        ],
        [
            KeyboardButton(text="◀️ Назад"),
        ],
    ],
    resize_keyboard=True
)