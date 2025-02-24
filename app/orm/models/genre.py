from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped
from orm.base import Base


# genreテーブルに対応するORMモデル
class Genre(Base):
    __tablename__ = "genre"

    id: Mapped[int] = Column(
        "id", TINYINT(unsigned=True), primary_key=True, autoincrement=True
    )
    name: Mapped[str] = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<Genre {self.name}>"
