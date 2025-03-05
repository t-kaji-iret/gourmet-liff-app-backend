import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from routers.review_router import session_factory
from main import app
from alembic.config import Config
from alembic import command

# マイグレーションの設定ファイルを指定
alembic_cfg = Config(os.path.abspath(__file__ + "/../../app/alembic.test.ini"))
os.chdir(os.path.abspath(__file__ + "/../../app"))

# テスト用DBに接続するための設定
test_engine = create_engine('mysql+pymysql://root:password@localhost:3306/test-gourmet-app', echo=True)
TestSession = sessionmaker(
    autocommit=False,
    autoflush=True,
    expire_on_commit=False,
    bind=test_engine
)


@pytest.fixture(scope="function")
def setup_db():
    print("✅✅✅✅✅✅✅")
    command.downgrade(alembic_cfg, "base")
    command.upgrade(alembic_cfg, "head")
    print("✅✅✅✅✅✅✅")

    def test_session_factory():
        test_session = TestSession()
        try:
            yield test_session
        finally:
            test_session.close()

    app.dependency_overrides[session_factory] = test_session_factory
