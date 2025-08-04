from database import SessionLocal

# DEPENDENCY FUNCTION
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()