import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import Base
from db import get_db
from main import app
from utils.token import get_current_user
from types import SimpleNamespace

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test_books.db"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args = {"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)


@pytest.fixture(scope = "session", autouse = True)
def create_test_database():
    print("Creating test tables......")
    Base.metadata.create_all(bind = engine)
    yield
    print("Dropping test tables........")
    Base.metadata.drop_all(bind = engine)


@pytest.fixture(scope = "function")
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope = "function")
def client(db_session):
    def override_get_db():
        print("Overridden get db called")
        yield db_session

    def override_get_current_user():
        return SimpleNamespace(
            id = 1,
            username = "testadmin",
            email = "testadmin@gmail.com",
            role = "admin"
        )
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_current_user

    with TestClient(app) as c:
        yield c