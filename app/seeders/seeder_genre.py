from sqlalchemy.orm import Session

from models.genre import Genre


def seed_master_data(session: Session):
    master_records = [
        Genre(id=1, name="中華"),
        Genre(id=2, name="イタリアン"),
        Genre(id=3, name="日本料理"),
    ]

    # 一括追加
    session.add_all(master_records)

    # コミットしてデータベースに保存
    session.commit()
