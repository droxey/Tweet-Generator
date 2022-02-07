"""
Module for creating lists of tokens from a text.
"""
from cleanup import remove_punctuation


def read_file(source_text):
    """Read in any body of text, remove punctuation, and turn it into a list."""
    if isinstance(source_text, list):
        return source_text

    word_list = []
    with open(source_text, mode='r', newline="\n") as _file:
        str = _file.read()
        clean_str = remove_punctuation(str)
        word_list = clean_str.split(' ')

    return word_list
