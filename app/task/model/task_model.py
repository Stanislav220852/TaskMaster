from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm  import relationship ,Mapped, mapped_column
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.user.model.user_model import UserModel
    from app.reminder.model.reminder_model import ReminderModel

class TaskModel(Base):
    title:Mapped[str]
    deadline:Mapped[str]
    is_complited:Mapped[bool]
    user_id:Mapped[int] = mapped_column(
        ForeignKey("usermodels.id"),
        index=True
    )
    user:Mapped["UserModel"] = relationship(back_populates="task")
    
    reminder:Mapped[list["ReminderModel"]] = relationship(back_populates="task")