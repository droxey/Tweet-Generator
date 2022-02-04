"""
Tweet Generator: Random Dictionary Words

$ python3 dictionary_words.py 3
wuss paragrammatist avitaminosis.

$ python3 dictionary_words.py 7
Nahuan semicynical Dendrobates madoqua semitangent rockstaff heptachronous.

$ python3 dictionary_words.py 4
polyoicous lupulin pennyrot boree.
"""
import sys
import random


OS_DICTIONARY = '/usr/share/dict/words'


def file_to_word_list(filename=OS_DICTIONARY):
    """Open a file and return a list of words."""
    words = []
    with open(filename, mode='r', newline="\n") as _file:
        for word in _file:
            words.append(word.rstrip())
    return words


def sample_random_words(corpus, number):
    """Return a list containing the indices of the selected sample words."""
    return random.sample(range(len(corpus)), k=number)


def build_random_sentence(corpus, samples):
    """Return a string containing the random words, with a period at the end."""
    return ' '.join([corpus[index] for index in samples]) + '.'


if __name__ == '__main__':
    number = 1 if len(sys.argv) <= 1 else int(sys.argv[1])
    corpus = file_to_word_list()
    sample = sample_random_words(corpus, number)
    sentence = build_random_sentence(corpus, sample)
    print(sentence)
