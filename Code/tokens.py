"""
Module for creating lists of tokens from a text.
"""
import re
from utils import ENGLISH_STOPWORDS


def split_on_whitespace(text):
    """Helper function that splits strings and removes all whitespace."""
    return re.split('\s+', text)


def remove_punctuation(text):
    """Helper function to remove undesirable characters from our corpus."""
    txt = re.sub('\[(.+)\]', ' ', text)  # Remove stage directions.
    txt = re.sub('[,;:—()]', '', txt)  # Remove punctuation.
    txt = re.sub('♪', '', txt)  # Remove music note.
    return txt


def remove_stopwords(text):
    return [word for word in text if word not in ENGLISH_STOPWORDS]


def tokenize(text):
    """Creates the tokens required by the Markov chain."""
    no_punc_text = remove_punctuation(text)
    words = split_on_whitespace(no_punc_text)
    tokens = remove_stopwords(words)
    return tokens


if __name__ == '__main__':
    import sys

    filename = 'data/sample.txt' if len(sys.argv) < 1 else sys.argv[1]
    source = open(filename).read()
    tokens = tokenize(source)
    print('CURRENT CORPUS:', filename)
    print(tokens)
