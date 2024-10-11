from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    DeclarativeBase
)
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import BigInteger


class Base(DeclarativeBase):
    pass


class AbstractModel(AsyncAttrs, Base):
    __tablename__ = ''