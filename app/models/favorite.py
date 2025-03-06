from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped
from base import Base
import datetime


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

    def __repr__(self) -> str:
        return f"<Favorite {self.id}>"
