from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, relationship
from app.orm.base import Base
import datetime
from orm.models.user import User


# reviewテーブルに対応するORMモデル
class Review(Base):
    __tablename__ = "review"

    id: Mapped[int] = Column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = Column(BIGINT(unsigned=True), nullable=False)
    restaurant_name: Mapped[str] = Column(String(255), nullable=False)
    nearest_station: Mapped[str] = Column(String(255), nullable=False)
    comment: Mapped[str] = Column(String(255), nullable=False)
    url: Mapped[str] = Column(String(255), nullable=True)
    created_at: Mapped[datetime.datetime] = Column(
        DateTime, default=datetime.datetime.utcnow
    )
    updated_at: Mapped[datetime.datetime] = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    user: Mapped[User] = relationship("User", back_populates="reviews")

    def __repr__(self) -> str:
        return f"<Genre {self.name}>"
