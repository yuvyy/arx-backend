from sqlmodel import Session
from app.models.models import User
from app.schemas.user import UserCreate,UserLogin
from app.core.security import verify_password

def createUser(db: Session, user: UserCreate):
    """
    Create a new user in the database.

    Args:
        db (Session): The database session.
        user (CreateUser): The user data to create.

    Returns:
        User: The created user object.
    """
    db_user = User(username=user.username, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    """
    Retrieve a user by their username.

    Args:
        db (Session): The database session.
        username (str): The username of the user to retrieve.

    Returns:
        User: The user object if found, None otherwise.
    """
    return db.query(User).filter(User.username == username).first()

def verify_user_password(db: Session, user: UserLogin):
    """
    Verify a user's password.

    Args:
        db (Session): The database session.
        username (str): The username of the user.
        password (str): The password to verify.

    Returns:
        User: The user object if the password is correct, None otherwise.
    """
    verified_user = db.query(User).filter(User.username == user.username).first()
    if user and verify_password(user.password, verified_user.hashed_password):
        return verified_user
    return None