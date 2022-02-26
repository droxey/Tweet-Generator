import random
import dictogram
import sampling


MARKOV_START_TOKEN = 'markovstart'
MARKOV_END_TOKEN = 'markovend'
MARKOV_TEST_ORDER = 2
MARKOV_TEST_DISTANCE = 10


class MarkovChain(object):
    """ A class that represents an nth order Markov Chain."""

    def __init__(self, corpus, order=1):
        """To create a new MarkovChain instance, pass a list representing the corpus, and optionally, the order."""
        self.corpus = corpus
        self.order = order
        self.sentence_tokens = [(MARKOV_START_TOKEN,)]
        self.markov_dict = dict()

        # Create word tuples:
        tuples, group = [], []
        for word_index in range(len(self.corpus) - self.order):
            for n in range(self.order):
                group.append(self.corpus[word_index + n])
                tuples.append((tuple(group), self.corpus[word_index +  self.order]))
                group = []

        # Add word tuples to self.markov_dict:
        for group in tuples:
            if group[0] in self.markov_dict:    # group[0] is the tuple, group[1] is the token
                self.markov_dict[group[0]].add_count(group[1])
            else:
                self.markov_dict[group[0]] = dictogram.Dictogram([group[1]])

    def walk(self, distance=None):
        """Walk the Markov Chain instance to generate a new sentence."""
        current = random.choice(self.sentence_tokens)
        output = []
        steps = 0
        walking = True

        while walking:
            word = sampling.sample(self.markov_dict[current])
            current = list(current[1:])
            current.append(word)
            current = tuple(current)
            walking = (distance is not None and steps <= distance) and (word != MARKOV_END_TOKEN)
            if walking:
                steps += 1
                output.append(word)

        return ' '.join(output)


if __name__ == '__main__':
    import pprint
    import tokens

    corpus = tokens.read_file('data/cats.txt')
    markov_chain = MarkovChain(corpus=corpus, order=MARKOV_TEST_ORDER)

    pprint.pprint(markov_chain.walk(MARKOV_TEST_DISTANCE))
