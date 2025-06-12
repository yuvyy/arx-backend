from sqlmodel import create_engine,Session, SQLModel

SQLALCHEMY_DATABASE_URL = "sqlite:///./../../../../arx.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # Only needed for SQLite
    echo=True,  # Set to True to see SQL queries in the console
)

def init_db():
    """
    Initialize the database by creating all tables.
    This should be called at the start of the application.
    """
    SQLModel.metadata.create_all(bind=engine)

def get_db():
    """
    Dependency that provides a database session.
    Yields a session and ensures it is closed after use.
    """
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()
