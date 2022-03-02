import os
import dotenv
dotenv.load_dotenv('.env')

from requests_oauthlib import OAuth1Session


# Authenticate with Twitter using the keys and tokens generated on the Developer Portal:
session = OAuth1Session(
    client_key=os.environ.get("TWITTER_CONSUMER_KEY"),
    client_secret=os.environ.get("TWITTER_CONSUMER_SECRET"),
    resource_owner_key=os.environ.get('TWITTER_ACCESS_TOKEN'),
    resource_owner_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))


# Twitter API URL for POSTing new tweets:
url = "https://api.twitter.com/2/tweets"


def tweet(status):
    # Make the request to post a new tweet:
    resp = session.post(url, json={ 'text': status })

    # If our request failed to create a tweet, throw an exception:
    if resp.status_code != 201:  # 201 = Created
        raise Exception("Request returned an error: {} {}".format(resp.status_code, resp.text))

    # Return the response in JSON format:
    return resp.text

if __name__ == '__main__':
    tweet('hello world')
