"""
Main script, uses other modules to generate sentences.
"""
from tokens import read_file
from dictogram import Dictogram
from flask import Flask


app = Flask(__name__)
word_list = read_file("data/fish.txt")
histo = Dictogram(word_list=word_list)
app.logger.info("loading word list")

@app.before_first_request
def before_first_request():
    app.logger.info("before_first_request")
    pass


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    app.logger.info("home")
    return histo.sample()


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
