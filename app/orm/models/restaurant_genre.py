from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped
from orm.base import Base


# restaurant_genreテーブルに対応するORMモデル
class RestaurantGenre(Base):
    __tablename__ = "restaurant_genre"

    id: Mapped[int] = Column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True
    )
    review_id: Mapped[int] = Column(BIGINT(unsigned=True), nullable=False)
    genre_id: Mapped[int] = Column(BIGINT(unsigned=True), nullable=False)

    def __repr__(self) -> str:
        return f"<RestaurantGenre {self.id}>"
