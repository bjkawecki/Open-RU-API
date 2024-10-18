from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///db.sqlite"
# DATABASE_URL = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/words"

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine, autocommit=False, autoflush=True) as session:
        yield session
