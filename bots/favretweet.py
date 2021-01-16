#!/usr/bin/env python
# tweepy-bots/bots/favretweet.py

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def favorite_tweets(api, keywords, since_id):
    logger.info('Favoriting and Retweeting tweets...')
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f'Favoriting and Retweeting: {tweet.text} by: {tweet.user.name}')

            if not tweet.user.following:
                tweet.user.follow()

            api.create_favorite(id=tweet.id)
            api.retweet(id=tweet.id)
    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = favorite_tweets(api, ['python', 'django'], since_id)
        logger.info('Waiting...')
        time.sleep(60)

if __name__ == '__main__':
    main()
