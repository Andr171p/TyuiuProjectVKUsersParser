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
    __tablename__ = 'candidates'

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class CandidatesModel(AbstractModel):
    ...