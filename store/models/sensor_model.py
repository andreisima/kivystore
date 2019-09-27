from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    String,
    Integer,
    Float
)

Base = declarative_base()


class Sensor(Base):
    __tablename__ = 'sensor'

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
        Float(4, 2),
        nullable=False
    )
