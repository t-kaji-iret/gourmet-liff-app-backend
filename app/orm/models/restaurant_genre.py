from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TINYINT, BIGINT
from sqlalchemy.orm import Mapped, relationship
from app.orm.base import Base
from orm.models.genre import Genre
from orm.models.review import Review


# restaurant_genreテーブルに対応するORMモデル
class RestaurantGenre(Base):
    __tablename__ = "restaurant_genre"

    id: Mapped[int] = Column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True
    )
    review_id: Mapped[int] = Column(BIGINT(unsigned=True), nullable=False)
    genre_id: Mapped[int] = Column(BIGINT(unsigned=True), nullable=False)

    review: Mapped[Review] = relationship("Review", back_populates="restaurant_genre")
    genre: Mapped[Genre] = relationship("Genre", back_populates="restaurant_genres")

    def __repr__(self) -> str:
        return f"<RestaurantGenre {self.id}>"
