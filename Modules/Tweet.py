__author__ = 'Antero'

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String, Sequence


class Tweet(Base):
    __tablename__ = 'tweet'
    id = Column(Integer, Sequence('tweet_id_seq'), primary_key=True)
    text = Column(String)

    def __repr__(self):
        return "<Tweet (text = %s)>" % (self.text.__repr__())
