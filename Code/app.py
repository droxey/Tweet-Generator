"""
Main script, uses other modules to generate sentences.
"""

from flask import Flask, redirect, render_template, request
from tokens import tokenize
from markov import MarkovChain
from twitter import tweet
from utils import MARKOV_TEST_ORDER, MARKOV_TEST_DISTANCE


CORPUS_FILE_NAME = 'data/corpus.txt'


app = Flask(__name__)
source = open(CORPUS_FILE_NAME).read()
tokens = tokenize(source)
chain = MarkovChain(tokens, order=MARKOV_TEST_ORDER)


@app.route('/')
def home():
    """Route that returns a web page containing the generated sentence."""
    sentence = chain.walk(distance=MARKOV_TEST_DISTANCE)
    return render_template('home.html', sentence=sentence)


@app.route('/tweet', methods=['POST'])
def tweet():
    tweet(request.form['sentence'])
    return redirect('/')


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
