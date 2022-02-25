import random


def sample(histogram):
    """Return a word from this histogram, randomly sampled by weighting
    each word's probability of being chosen by its observed frequency."""
    distance = 0
    dart = random.uniform(0, histogram.tokens)
    for word, count in histogram.items():
        distance += count
        if distance >= dart:
            return word
