from sqlalchemy import (
    Column, Integer, SmallInteger, String, Text, Float, BigInteger,
    CHAR
)
from db.db_connect import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(Text, nullable=False, default='')
    password = Column(Text, nullable=False, default='')
