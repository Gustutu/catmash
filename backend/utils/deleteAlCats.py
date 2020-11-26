from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, LargeBinary, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from struct import *
import json
import os
import requests


Base = declarative_base()
engine_string = os.getenv('PROD_DATABASE_URL')
engine = create_engine(engine_string, echo=True)


class Cat(Base):
    __tablename__ = 'cats'
    id = Column(String, primary_key=True)

    # image = Column(LargeBinary)

    score = Column(Integer)


Session = sessionmaker(bind=engine)
session = Session()
session.query(Cat).delete()

session.commit()