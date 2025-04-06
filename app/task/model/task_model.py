from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm  import relationship ,Mapped, mapped_column
from typing import TYPE_CHECKING,List


if TYPE_CHECKING:
    from app.user.model.user_model import UserModel
    from app.reminder.model.reminder_model import ReminderModel

class TaskModel(Base):
    title:Mapped[str] = mapped_column(default="Задача")
    deadline:Mapped[str] = mapped_column(default="0000-00-00")
    is_complited:Mapped[bool] = mapped_column(default=False)
    user_id:Mapped[int] = mapped_column(
        ForeignKey("usermodels.id",ondelete="cascade"),
        index=True
    )
    user:Mapped["UserModel"] = relationship(back_populates="task")
    
    reminder:Mapped[List["ReminderModel"]] = relationship("ReminderModel",back_populates="task")