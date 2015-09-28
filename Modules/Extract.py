__author__ = 'Antero'

from Twitter import Twitter
from Inst import Instagram
from Load import Load

class Extract:
    def __init__(self):
        print 'Starting extraction'
        self.instagram = Instagram()
        self.load = Load()

    def extract_twitter(self, accounts):
        print 'Starting Twitter extraction'
        for account in accounts:
            twitter = Twitter(account=account)
            for tweet in twitter.home_timeline():
                self.load.save_tweet(text = tweet.text)

    def extract_instagram(self,accounts):
        print 'Starting Instagram extraction'
        for account in accounts:
            user = self.instagram.get_user(name = account)
            media = self.instagram.get_media(user_id = user.id)


