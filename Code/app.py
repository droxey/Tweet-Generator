"""
Main script, uses other modules to generate sentences.
"""
from flask import Flask
from tokens import read_file
from markov import MarkovChain


MARKOV_WALK_DISTANCE = 10


app = Flask(__name__)
word_list = read_file("data/corpus.txt")
markov_chain = MarkovChain(word_list, order=2)


@app.route("/")
def home():
    """Route that returns a web page containing the generated sentence."""
    return markov_chain.walk(distance=MARKOV_WALK_DISTANCE)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
