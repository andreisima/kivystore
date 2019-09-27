from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
)

Base = declarative_base()


class Switch(Base):
    __tablename__ = 'switch'

    uuid = Column(
        'uuid',
        Integer,
        primary_key=True,
        nullable=False
    )
    name = Column(
        'name',
        String(10),
        nullable=False
    )
    human_name = Column(
        'human_name',
        String(50),
        nullable=False
    )
    value = Column(
        'value',
        Boolean,
        nullable=False
    )
    updated_at = Column(
        'updated_at',
        DateTime,
        nullable=False
    )
