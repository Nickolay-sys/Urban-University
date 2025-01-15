from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmarker, DeclarativeBase

engine = create_engine("sqlite:///taskmanager.db", echo=True)

SesionLocal = sessionmarker(bind=engine)
class Base(DeclarativeBase):
    pass