import random
from dictogram import Dictogram
from sampling import sample


MARKOV_TEST_ORDER = 2
MARKOV_TEST_DISTANCE = 15


class MarkovChain(object):
    """ A class that represents an nth order Markov chain."""
    MARKOV_END_TOKEN = 'MARKOVEND'

    def __init__(self, corpus, order=1):
        """To create a new MarkovChain instance, pass a list representing the corpus, and optionally, the order."""
        # Store the Markov chain in a dictionary.
        self.chain = dict()
        self.windows = list()

        # Range over corpus length - order (avoid IndexErrors!)
        for word_index in range(len(corpus) - order):
            # Store the word window as a list.
            word_list = []
            # Range over the order integer.
            for n in range(order):
                # Append until the length of word_list == n.
                word_list.append(corpus[word_index + n])

            # Once we've collected the word list, convert it to a tuple.
            window = tuple(word_list)

            # Add the window to a list of windows (we'll use this later to walk)
            self.windows.append(window)

            # Grab the nth word from the corpus.
            nth_word = corpus[word_index + order]
            # If exists, add the nth_word to the count.
            if window in self.chain:
                self.chain[window].add_count(nth_word)
            else:
                # Otherwise, create a new instance of the Dictogram,
                # and initialize it with the nth_word.
                self.chain[window] = Dictogram([nth_word])

    def walk(self, distance=10):
        """Walk the Markov Chain instance to generate a new sentence."""
        # Set window to the starting point at the beginning of the walk.
        window = random.choice(self.windows)
        words = []  # A place to hold the sentence as we generate it.
        walking = True  # Set to true to walk when called.

        while walking:
            word = sample(self.chain[window])
            window_list = list(window[1:])
            window_list.append(word)
            window = tuple(window_list)
            walking = word != self.MARKOV_END_TOKEN and len(words) < distance
            if walking:
                words.append(word)

        # Join the list of words to return a sentence.
        return ' '.join(words) + '.'


if __name__ == '__main__':
    import tokens
    import pprint

    corpus = tokens.read_file(
        '/Users/droxey/dev/repos/ACS/grading/runthru/Code/data/cats.txt')
    markov_chain = MarkovChain(corpus=corpus, order=MARKOV_TEST_ORDER)

    print("MARKOV CHAIN:")
    pprint.pprint(markov_chain.chain, indent=4)
    print("=" * 120)
    print(f"START WINDOW: {markov_chain.start_window}")
    print(f"RANDOM WALK: {markov_chain.walk(MARKOV_TEST_DISTANCE)}")
