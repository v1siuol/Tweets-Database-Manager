from faker import Faker
from random import randint
from app.db_models import Tweet
from sqlalchemy.exc import IntegrityError
from app.config import config
from app.db_manager import Manager


# session = Session()
# print(session)
# BUG  to-do class fake

def tweet(session, count=1):
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
    manager = Manager()
    session = manager.Session()
    # print(session)

    tweet(session, 1)
    print('-- DONE --')

