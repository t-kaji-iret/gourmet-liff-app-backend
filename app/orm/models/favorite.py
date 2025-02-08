from typing import List
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, relationship
from app.orm.base import Base
import datetime
from orm.models.review import Review
from orm.models.user import User


# favoriteテーブルに対応するORMモデル
class Favorite(Base):
    __tablename__ = "favorite"

    id: Mapped[int] = Column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True
    )
    review_id: Mapped[int] = Column(BIGINT, nullable=False)
    user_id: Mapped[int] = Column(BIGINT, nullable=False)
    created_at: Mapped[datetime.datetime] = Column(
        DateTime, default=datetime.datetime.utcnow
    )

    reviews: Mapped[List[Review]] = relationship("Review", back_populates="favorites")
    user: Mapped[User] = relationship("User", back_populates="favorites")

    def __repr__(self) -> str:
        return f"<Favorite {self.id}>"
