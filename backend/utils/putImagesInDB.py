from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, LargeBinary, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from struct import *
import json
import requests


Base = declarative_base()
engiene_string = 'mysql+pymysql://catUser:Catmdp1234?@127.0.0.1/cats'
engine = create_engine(engiene_string, echo=True)


class Cat(Base):
    __tablename__ = 'cats'
    id = Column(String, primary_key=True)

    image = Column(LargeBinary)

    score = Column(Integer)


Session = sessionmaker(bind=engine)
session = Session()

# Add just one test cat in database
# cat = Cat(id='ed', image=pack('H', 365))
# session.add(cat)
# session.commit()

with open('cats.json') as json_file:
    data = json.load(json_file)


# Download and add first cat in DB
# cat = data["images"][1]
# data = requests.get(cat["url"]).content
# session.add((Cat(id=cat["id"], image=data)))
# session.commit()


for cat in data["images"]:
    print("downloading"+cat["url"])
    data = requests.get(cat["url"]).content
    session.add((Cat(id=cat["id"], image=data)))

session.commit()
