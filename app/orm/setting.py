import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from collections.abc import Generator

if os.getenv('STAGE') == 'local':
    engine = create_engine('mysql+pymysql://admin:password@localhost:3306/gourmet-app-db', echo=True)
else:
    # TODO: RDSのエンドポイントを設定する
    pass

Session = sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine
)


@contextmanager
def session_factory() -> Generator[Session, None, None]:
    session = Session()
    e = None
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        if e is None:
            session.commit()
        session.close()
