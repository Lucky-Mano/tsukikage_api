"""User table."""
from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):  # type: ignore
    """User table."""

    __tablename__ = "user"

    id = Column(UUID, primary_key=True)
    name = Column(Text)
    hashed = Column(Text)
    serial = Column(Text)
    mail = Column(Text)
