from dictogram import Dictogram
from sampling import sample


MARKOV_TEST_ORDER = 2
MARKOV_TEST_DISTANCE = 15


class MarkovChain(object):
    """ A class that represents an nth order Markov chain."""
    MARKOV_START_TOKEN = 'markovstart'      # Add this token to any corpus to indicate the entry point.
    MARKOV_END_TOKEN = 'markovend'          # Add this token to any corpus to indicate the exit point.

    def __init__(self, corpus, order=1):
        """To create a new MarkovChain instance, pass a list representing the corpus, and optionally, the order."""
        self.chain = dict()                 # Store the Markov chain in a dictionary.
        self.start_window = None            # A tuple that represents the starting point of our sentence.

        for word_index in range(len(corpus) - order):       # Range over corpus length - order (avoid IndexErrors!)
            word_list = []                                  # Store the word window as a list.
            for n in range(order):                          # Range over the order integer.
                word_list.append(corpus[word_index + n])    # Append until the length of word_list == n.

            window = tuple(word_list)                       # Once we've collected the word list, convert it to a tuple.
            if window[0] == self.MARKOV_START_TOKEN:        # word_tuple[0] contains the 1st word in the tuple.
                self.start_window = window                  # Set the start window based on MARKOV_START_TOKEN.

            nth_word = corpus[word_index + order]           # Grab the nth word from the corpus.
            if window in self.chain:                        # If exists, add the nth_word to the count.
                self.chain[window].add_count(nth_word)
            else:                                           # Otherwise, create a new instance of the Dictogram.
                self.chain[window] = Dictogram([nth_word])

    def walk(self, distance=None):
        """Walk the Markov Chain instance to generate a new sentence."""
        words = []                          # A place to hold the sentence as we generate it.
        window = self.start_window          # Set window to the starting point at the beginning of the walk.
        walking = True                      # Set to true to walk when called.

        while walking:
            word = sample(self.chain[window])
            window_list = list(window[1:])
            window_list.append(word)
            window = tuple(window_list)
            walking = word != self.MARKOV_END_TOKEN and (distance is not None and len(words) < distance)
            if walking:
                words.append(word)

        return ' '.join(words) + '.'        # Join the list of words to return a sentence.


if __name__ == '__main__':
    import tokens
    import pprint

    corpus = tokens.read_file('/Users/droxey/dev/repos/ACS/grading/runthru/Code/data/cats.txt')
    markov_chain = MarkovChain(corpus=corpus, order=MARKOV_TEST_ORDER)

    print("MARKOV CHAIN:")
    pprint.pprint(markov_chain.chain, indent=4)
    print("=" * 120)
    print(f"START WINDOW: {markov_chain.start_window}")
    print(f"RANDOM WALK: {markov_chain.walk(MARKOV_TEST_DISTANCE)}")
