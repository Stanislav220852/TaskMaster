from app.db.base import Base
from sqlalchemy import BIGINT,Column
from sqlalchemy.orm  import relationship ,Mapped
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.task.model.task_model import TaskModel


class UserModel(Base):
    telegram_id = Column(BIGINT)
    language = Mapped[str]

    task: Mapped[list["TaskModel"]] = relationship(back_populates="user")

