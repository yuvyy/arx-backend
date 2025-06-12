from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a password using PBKDF2 with SHA256.
    """
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify a password against a hashed password.
    
    Args:
        password (str): The plain text password to verify.
        hashed_password (str): The hashed password to compare against.
    
    Returns:
        bool: True if the password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(password, hashed_password)