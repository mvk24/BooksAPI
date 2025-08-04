from sqlalchemy import Column, Integer, String, Float
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, unique = True, index = True, nullable = False)
    author = Column(String, nullable = False)
    genre = Column(String, nullable = True)
    yop = Column(Integer, nullable = True)
    description = Column(String, nullable = True)
    price = Column(Float, nullable = True)