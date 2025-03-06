from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped
from base import Base
import datetime


# review_imageテーブルに対応するORMモデル
class ReviewImage(Base):
    __tablename__ = "review_image"

    id: Mapped[int] = Column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True
    )
    review_id: Mapped[int] = Column(BIGINT(unsigned=True), nullable=False)
    path: Mapped[str] = Column(String(255), nullable=False)
    thumbnail_flg: Mapped[bool] = Column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime.datetime] = Column(
        DateTime, default=datetime.datetime.utcnow
    )

    def __repr__(self) -> str:
        return f"<ReviewImage {self.id}>"
