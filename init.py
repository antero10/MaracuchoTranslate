__author__ = 'Antero'

from Modules.Extract import Extract
from Modules.Config import Config

extract = Extract()
config = Config()

extract.extract_twitter(config.twitter_accounts)
#extract.extract_instagram(config.instagram_accounts)