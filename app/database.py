import contextlib
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

if os.getenv('STAGE') == 'local':
    engine = create_engine('mysql+pymysql://root:password@gourmet-app-db:3306/gourmet-app', echo=True)
else:
    # TODO: RDSのエンドポイントを設定する
    pass

Session = sessionmaker(
    autocommit=False,
    autoflush=True,
    expire_on_commit=False,
    bind=engine
)


def session_factory() -> Session:
    session = Session()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        session.close()
