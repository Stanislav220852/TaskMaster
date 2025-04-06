from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm  import relationship ,Mapped, mapped_column
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.task.model.task_model import TaskModel

class ReminderModel(Base):
    cron_expression = Mapped[str]
    scheduled_time:Mapped[str]
    task_id:Mapped[int] = mapped_column(
        ForeignKey("taskmodels.id"),
        index=True
    )
    task:Mapped["TaskModel"] = relationship(back_populates="reminder")
    
