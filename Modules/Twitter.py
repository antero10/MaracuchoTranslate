__author__ = 'Antero'

import tweepy


class Twitter:
    def __init__(self, account=''):
        auth = tweepy.OAuthHandler("0nXXTL5b6ibmPrjciZHVdM6Hp", "feFympkn2xexueGChOir7kXBowwgG4pM0k9e31NCVA93Jp9E6W")
        auth.set_access_token("79949444-mZuLoxfj4RTqL5lKIx8oVraTK3PpaEalj6LjWxRZZ",
                              "nunctrC1YduXdkPTw0M46pM4rhtdZuE126pflyWdYb4dJ")
        self.api = tweepy.API(auth)
        self.account = account

    def home_timeline(self):
        return self.api.user_timeline(id=self.account)
