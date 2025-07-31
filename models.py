from sqlalchemy import Column, Integer, String, Float
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    author = Column(String)
    genere = Column(String)
    yop = Column(Integer)
    description = Column(String)
    price = Column(Float)