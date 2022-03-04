"""
Main script, uses other modules to generate sentences.
"""
import twitter
from flask import Flask, redirect, render_template, request
from tokens import tokenize
from markov import MarkovChain
from utils import MARKOV_TEST_ORDER


MARKOV_WALK_DISTANCE = 30
CORPUS_FILE_NAME = 'data/snippet.txt'


app = Flask(__name__)
source = open(CORPUS_FILE_NAME).read()
tokens = tokenize(source)
chain = MarkovChain(tokens, order=MARKOV_TEST_ORDER)


@app.route('/')
def home():
    """Route that returns a web page containing the generated sentence."""
    sentence = chain.walk(distance=MARKOV_WALK_DISTANCE)
    return render_template('home.html', sentence=sentence)


@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
