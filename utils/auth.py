from passlib.context import CryptContext


# Password Hashing
pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

# Hash Password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify the Password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
