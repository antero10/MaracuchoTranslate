__author__ = 'Antero'

from Tweet import Tweet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class Load:
    def __init__(self):
        engine = create_engine('mysql://root:root@192.168.99.100/maracuchoExtract')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def save_tweet(self, text):
        tweet = Tweet(text=text.__repr__())
        print tweet
        self.session.add(tweet)
        self.session.commit()
