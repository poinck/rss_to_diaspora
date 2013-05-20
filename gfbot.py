#!/usr/bin/python -u
from rssbot import RSSBot
import configparser

gf_feed = 'http://gnufunzt.de/rss2.xml'

config = configparser.ConfigParser()
config.read('config')

pod = config['GF']['pod']
user = config['GF']['user']
password = config['GF']['password']

if __name__ == '__main__':
    gfbot = RSSBot(gf_feed, ['#gnufunzt'], pod, user, password)
    gfbot.start()
