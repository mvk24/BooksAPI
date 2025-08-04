from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"       #Name of the tabl in database

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True, index = True, nullable = False)
    email = Column(String, unique = True, index = True, nullable = True)
    hashed_password = Column(String, nullable = False)