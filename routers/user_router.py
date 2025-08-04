from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from schemas.user_schema import UserCreate, UserOut, UserUpdate
from models.user_model import User
from utils.auth import hash_password
from db import get_db
from typing import List

router = APIRouter(prefix = "/users", tags = ["Users DB"])


# Create a new user
@router.post("/", response_model = UserOut, status_code = 201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        or_(
            User.email == user.email,
            User.username == user.username
        )
    ).first()

    if existing_user:
        raise HTTPException(status_code = 400, detail = "Email or Username already registered")
    

    hashed_pw = hash_password(user.password)

    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user




# Get all Users
@router.get("/", response_model = List[UserOut], summary = "List of Users", description = "List of Registered Users in DB" , response_description = "Registered Users")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# Get by User ID
@router.get("/{user_id}", response_model = UserOut, summary = "Get User by ID", description = "Get user details by ID")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found")
    return user


# Search by username and/or email
@router.get("/search/", response_model = List[UserOut], summary = "Search by User Name/Email", description = "Filter by User Name AND/OR by Email")
def search_user(username: str = None, email: str = None, db: Session = Depends(get_db)):
    query = db.query(User)
    if username:
        query = query.filter(User.username.ilike(f"%{username}%"))
    if email:
        query = query.filter(User.email.ilike(f"%{email}%"))
        
    res = query.all()
    return res



# Update User Details
@router.put("/{user_id}", response_model = UserOut, summary = "Update User details", description = "Update the User details")
def update_user(user_id: int, new_user_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found")
    for key, value in new_user_data.model_dump(exclude_unset = True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user




# Delete user by ID
@router.delete("/{user_id}", summary = "Delete User By ID", description = "Delete the User details by ID")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully",
            "Deleted User": {
                "id": user.id,
                "username": user.username,
                "email": user.email
                }
            }