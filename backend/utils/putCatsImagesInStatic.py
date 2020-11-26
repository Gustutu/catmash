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
cat = data["images"][1]
for cat in data["images"]:
    data = requests.get(cat["url"]).content
    file_name = cat["id"]
    f = open("/home/gustutu/catmash/django-vue-template/public/static/"+file_name, "wb")
    f.write(data)
    f.close()
    

