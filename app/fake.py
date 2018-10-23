"""
Description: Dump data to db
Author: Zhaohong Lyu
Last Modified: 2018/10/22
"""

from faker import Faker
from random import randint
from models import Tweet
from sqlalchemy.exc import IntegrityError
from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_connector import Session
from geoalchemy2 import Geometry


session = Session()
print(session)


def tweet(count=1):
    fake = Faker()
    # db.session.rollback()
    i = 0
    while i < count:
        t = Tweet(user_name=fake.name(),
                  #  coordinate='POINT(1 1)',
                  tweet=fake.text(),
                  sentiment=1,
                  )
        session.add(t)
        try:
            session.commit()
            i += 1
        except IntegrityError:
            session.rollback()


if __name__ == '__main__':
    tweet()
    print('-- DONE --')

