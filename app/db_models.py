from sqlalchemy import Column, Integer, String, Text
# from geoalchemy2 import Geometry
from app.db_manager import Manager


# todo
# Coordinate two array

class Tweet(Manager.Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(150))
    #  coordinate = Column(Geometry('POINT')) 
    tweet = Column(Text)
    sentiment = Column(Integer)
   
    def __repr__(self):
        # return '<Id: %d # Name: %r # Point: %s # Senti: %d # Tweet: %s>' % (self.id, self.user_name, self.coordinate, self.sentiment, self.tweet)
        return '<Id: %d # Name: %r # Senti: %d # Tweet: %s>' % (self.id, self.user_name, self.sentiment, self.tweet)


