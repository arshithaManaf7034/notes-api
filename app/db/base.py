from sqlalchemy.orm import DeclarativeBase
from app.db.base_class import Base

from app.models.user import User
from app.models.note import Note


class Base(DeclarativeBase):
    pass
