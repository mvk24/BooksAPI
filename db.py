from typing import Dict


# FAKE IN MEMORY DATABASE (DEPENDENCY INJECTION)
fake_books_db: Dict[int, dict] = {}


# DEPENDENCY FUNCTION
def get_db():
    return fake_books_db