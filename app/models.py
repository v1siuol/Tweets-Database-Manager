"""
Description: database table models
Author: Zhaohong Lyu
Last Modified: 2018/10/22
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 
from geoalchemy2 import Geometry


Base = declarative_base()


class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(150))
    #  coordinate = Column(Geometry('POINT')) 
    tweet = Column(String(150))
    sentiment = Column(Integer)
   
    def __repr__(self):
        return '<Id: %d # Name: %r # Point: %s # Senti: %d # Tweet: %s>' % (self.id, self.user_name, self.coordinate, self.sentiment, self.tweet)


