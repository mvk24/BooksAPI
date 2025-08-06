from fastapi import Depends, HTTPException, status
from models.user_model import User
from utils.token import get_cuurent_user

def admin_only(current_user: User = Depends(get_cuurent_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code = 403, detail = "Admins Only : You are not authorized tonperform this action.")
    return current_user