from database import SessionLocal

# DEPENDENCY FUNCTION
def get_db():
    print("Original get db called")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()