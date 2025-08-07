from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"       #Name of the table in database

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True, index = True, nullable = False)
    email = Column(String, unique = True, index = True, nullable = True)
    hashed_password = Column(String, nullable = False)
    role = Column(String, default = "user")

    books = relationship("Book", back_populates = "owner")