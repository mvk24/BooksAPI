from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db import get_db
from models.user_model import User
from utils.auth import authenticate_user
from utils.token import create_access_token
from schemas.token_schema import TokenResponse
from datetime import timedelta

router = APIRouter(prefix = "/auth", tags = ["Authentication"])

@router.post("/login", response_model = TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code = 403, detail = "Invalid Username or password.")

    # JWT Token Creating
    access_token = create_access_token(data = {"sub": user.username})
    return {"access_token": access_token,
            "token_type": "bearer"
            }
