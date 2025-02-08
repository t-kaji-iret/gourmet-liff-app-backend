from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, relationship
from app.orm.base import Base
import datetime
from orm.models.user import User
from orm.models.review import Review


# replyテーブルに対応するORMモデル
class reply(Base):
    __tablename__ = "reply"

    id: Mapped[int] = Column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True
    )
    review_id: Mapped[int] = Column(BIGINT(unsigned=True), nullable=False)
    user_id: Mapped[int] = Column(BIGINT(unsigned=True), nullable=False)
    body: Mapped[str] = Column(String(255), nullable=False)
    created_at: Mapped[datetime.datetime] = Column(
        DateTime, default=datetime.datetime.utcnow
    )
    updated_at: Mapped[datetime.datetime] = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    review: Mapped[Review] = relationship("Review", back_populates="replies")
    user: Mapped[User] = relationship("User", back_populates="replies")

    def __repr__(self) -> str:
        return f"<Genre {self.id}>"
