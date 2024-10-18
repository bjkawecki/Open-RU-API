from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite"
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/words"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)

Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
metadata = Base.metadata


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
