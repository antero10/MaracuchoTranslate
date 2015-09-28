__author__ = 'Antero'

import yaml

class Config:
    def __init__(self):
        config_file = open('config.yaml', 'r')
        config = yaml.load(config_file)
        self.twitter_accounts = config[0]['twitter_accounts']
        self.instagram_accounts = config[0]['instagram_accounts']
