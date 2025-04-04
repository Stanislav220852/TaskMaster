from sqlalchemy import select
from app.db.engine import new_session
from app.user.model.user_model import UserModel

class UserServices:
    @classmethod
    async def add_user(cls,telegram_id:int,language:str = "ru"):
        async with new_session() as session:
            result = await session.execute(select(UserModel).where(UserModel.telegram_id == telegram_id))
            user = result.scalars().first()
            if not user:
                user = UserModel(telegram_id == telegram_id,
                                    language == language)
                
            session.add(user)
            await session.commit()
            await session.refresh(user)

        return user