from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from app.core.config import settings
from app.db.base import Base
from app.reminder.model.reminder_model import ReminderModel
from app.task.model.task_model import TaskModel
from app.user.model.user_model import UserModel


engine = create_async_engine(
    url= settings.DB_URL
)

new_session = async_sessionmaker(engine,
    expire_on_commit= settings.DB_EXPIRE_ON_COMMIT,
    autoflush= settings.DB_AUTOFLUSH,
)

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
