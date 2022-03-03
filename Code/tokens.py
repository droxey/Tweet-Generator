"""
Module for creating lists of tokens from a text.
"""
import re
from nltk.corpus import stopwords


def split_on_whitespace(text):
    """Helper function that splits strings and removes all whitespace."""
    return re.split('\s+', text)


def remove_punctuation(text):
    """Helper function to remove undesirable characters from our corpus."""
    txt = re.sub('\[(.+)\]', ' ', text)  # Remove stage directions.
    txt = re.sub('[,;:—()]', '', txt)  # Remove punctuation.
    txt = re.sub('♪', '', txt)  # Remove music note.
    return txt


def tokenize(text):
    """Creates the tokens required by the Markov chain."""
    no_punc_text = remove_punctuation(text)
    words = split_on_whitespace(no_punc_text)
    tokens = [word for word in words if word not in stopwords.words('english')]
    return tokens


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        tokens = tokenize(source)
        print(tokens)
    else:
        print('No source text filename given as argument')
