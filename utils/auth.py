from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.user_model import User


# Password Hashing
pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")


# Hash Password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify the Password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, username: str, password: str):

    print("Fetching user from DB with username:", username)
    user = db.query(User).filter(func.lower(User.username) == username.lower()).first()
    print("User fetched from DB:", user)
    if not user:
        print("User not found")
        return False
    
    print("Stored password in DB:", user.hashed_password)
    print("Password entered:", password)
    print("Paasword match result:", verify_password(password, user.hashed_password))

    
    if  not verify_password(password, user.hashed_password):
        print("Password mismatch")
        return False
    
    return user
    
    