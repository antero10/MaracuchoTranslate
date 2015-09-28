__author__ = 'Antero'

from instagram.client import InstagramAPI


class Instagram:
    def __init__(self):
        access_token = "1c7300cd9baa4ebb875cf970450ea49a"
        client_secret = "773cba503f6a4056bf2610d01077dfcb"
        self.api = InstagramAPI(client_id=access_token, client_secret=client_secret)

    def search(self, account):
        return self.api.user_search(q=account, count=1)

    def get_user(self, name):
        user = self.search(name)

        return user[0]

    def get_media(self, user_id, count = 10):
        return self.api.user_recent_media(user_id=user_id, count=count)
