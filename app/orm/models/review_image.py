from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, relationship
from app.orm.base import Base
import datetime
from orm.models.review import Review
from orm.models.user import User


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

    review: Mapped[Review] = relationship("Review", back_populates="review_images")

    def __repr__(self) -> str:
        return f"<ReviewImage {self.id}>"
