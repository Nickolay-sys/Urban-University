from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///taskmanager.db", echo=True)

SesionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass