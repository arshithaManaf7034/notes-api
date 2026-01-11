from app.db.base import Base
from app.db.session import engine

# IMPORTANT: import all models here
from app.models.user import User
from app.models.note import Note

def init_db():
    Base.metadata.create_all(bind=engine)

