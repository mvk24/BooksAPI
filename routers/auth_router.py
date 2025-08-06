from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db import get_db
from models.user_model import User
from utils.auth import authenticate_user, hash_password
from utils.token import create_access_token
from schemas.token_schema import TokenResponse
from schemas.user_schema import UserCreate, UserOut, SelfRegister
from dependencies.roles import admin_only

router = APIRouter(prefix = "/auth", tags = ["Authentication"])

@router.post("/login", response_model = TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code = 403, detail = "Invalid Username or password.")

    # JWT Token Creating
    access_token = create_access_token(data = {"username": user.username, "role": user.role})

    return {"access_token": access_token,
            "token_type": "bearer"
            }


@router.post("/signup", response_model = TokenResponse)
def signup(user: SelfRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code = 400, detail = "Username already exists")
    hashed_pw = hash_password(user.password)

    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_pw,
        role = "user"   #Only new users can be self registerd, thus forcefulmdefault user role assign
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # JWT Token Creating
    access_token = create_access_token(data = {"username": new_user.username, "role": new_user.role})

    return {"access_token": access_token,
            "token_type": "bearer"
            }