from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped
from base import Base
import datetime


# replyテーブルに対応するORMモデル
class Reply(Base):
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

    def __repr__(self) -> str:
        return f"<Genre {self.id}>"
