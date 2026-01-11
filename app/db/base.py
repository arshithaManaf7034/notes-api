from sqlalchemy.orm import DeclarativeBase
from app.db.base import Base

from app.models.user import User
from app.models.note import Note


class Base(DeclarativeBase):
    pass
