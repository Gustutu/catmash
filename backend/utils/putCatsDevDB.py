from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, LargeBinary, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from struct import *
import json
import requests


Base = declarative_base()
engine_string = 'mysql+pymysql://catUser:Catmdp1234?@127.0.0.1/cats'
engine = create_engine(engine_string, echo=True)


class Cat(Base):
    __tablename__ = 'cats'
    id = Column(String, primary_key=True)

    # image = Column(LargeBinary)

    score = Column(Integer)


Session = sessionmaker(bind=engine)
session = Session()


with open('cats.json') as json_file:
    data = json.load(json_file)

for cat in data["images"]:
    print("downloading"+cat["url"])
    session.add((Cat(id=cat["id"], score=100)))

session.commit()

