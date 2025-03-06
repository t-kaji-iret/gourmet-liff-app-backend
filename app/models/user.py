from typing import List
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import TINYINT, BIGINT
from sqlalchemy.orm import Mapped, relationship
from base import Base
import datetime


# userテーブルに対応するORMモデル
class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = Column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True
    )
    line_user_id: Mapped[str] = Column(String(255), nullable=False)
    name: Mapped[str] = Column(String(255), nullable=False)
    email: Mapped[str] = Column(String(255), nullable=False)
    tel: Mapped[int] = Column(TINYINT(unsigned=True), nullable=False)
    created_at: Mapped[datetime.datetime] = Column(
        DateTime, default=datetime.datetime.utcnow
    )
    updated_at: Mapped[datetime.datetime] = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    def __repr__(self) -> str:
        return f"<User {self.id}>"
