import os
from requests_oauthlib import OAuth1Session
import dotenv
dotenv.load_dotenv('.env')

# Authenticate with Twitter using the keys and tokens generated on the Developer Portal:
# https://developer.twitter.com/en/portal/dashboard
session = OAuth1Session(
    client_key=os.environ.get("TWITTER_CONSUMER_KEY"),
    client_secret=os.environ.get("TWITTER_CONSUMER_SECRET"),
    resource_owner_key=os.environ.get('TWITTER_ACCESS_TOKEN'),
    resource_owner_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))


def tweet(status):
    # Create a request to post a new tweet:
    resp = session.post("https://api.twitter.com/2/tweets",
                        json={'text': status})

    # If our request failed to create a tweet, throw an exception:
    if resp.status_code != 201:  # 201 = Created
        raise Exception("Request returned an error: {} {}".format(
            resp.status_code, resp.text))

    return resp.text  # Return the response in JSON format


if __name__ == '__main__':
    import sys
    from markov import MarkovChain
    from tokens import tokenize
    from utils import MARKOV_TEST_ORDER, MARKOV_TEST_DISTANCE

    filename = 'data/sample.txt' if len(sys.argv) < 1 else sys.argv[1]
    source = open(filename).read()
    tokens = tokenize(source)
    chain = MarkovChain(tokens, order=MARKOV_TEST_ORDER)
    sentence = chain.walk(distance=MARKOV_TEST_DISTANCE)

    print('CORPUS: ', filename)
    print('TWEETING: ', sentence)
    tweet(sentence)
