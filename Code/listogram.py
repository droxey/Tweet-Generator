#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def search(self, word):
        """Look for a word in a listogram. Return None if not found."""
        for index, word_and_count in enumerate(self):
            if word_and_count[0] == word:
                return word_and_count, index
        return None, 0

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        word = str(word)
        found_word_count, index = self.search(word)
        if found_word_count:
            new_word_count = found_word_count[1] + int(count)
            self[index] = [word, new_word_count]
        else:
            self.append([word, int(count)])
            self.types += 1
        self.tokens += int(count)

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        found_word_count, _ = self.search(word)
        return 0 if not found_word_count else found_word_count[1]

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        found_word, _ = self.search(word)
        return found_word is not None

    def index_of(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        found_word_count, index = self.search(target)
        return index if found_word_count else None

    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        target = 0
        dart = random.uniform(0, self.tokens)
        for word_and_count in self:
<<<<<<< HEAD
            if target <= dart:
                target += word_and_count[1]
=======
>>>>>>> 2274d3d ([add] tweet generator code)
            if target >= dart:
                return word_and_count[0]


def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram:
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(
            error) < 0.1 else red
        print('| {!r:<9} '.format(word)
              + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
              + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
              + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
