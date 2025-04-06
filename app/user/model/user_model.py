from app.db.base import Base
from sqlalchemy import BIGINT, BigInteger,Column
from sqlalchemy.orm  import relationship ,Mapped,mapped_column
from typing import TYPE_CHECKING
from typing import List

if TYPE_CHECKING:
    from app.task.model.task_model import TaskModel


class UserModel(Base):
    telegram_id =Mapped[int]= mapped_column(nullable=False, unique=True)
    language = Mapped[str]

    task: Mapped[list["TaskModel"]] = relationship(back_populates="user")

