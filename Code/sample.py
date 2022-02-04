"""
# Module for generating a sample word from a histogram.
"""
import random
from histogram import get_argument, dictogram, listogram


def sampler(histogram):
    """Returns a random word weighted upon frequency."""
    total = 0
    # if isinstance(histogram, dict):
    #     for key, value in histogram.items():
    #         left = total
    #         right = total + value
    #         total = right
    #     dart = random.randint(0, total)
    #     if dart >= left:
    #         print("WORD:", key, "LEFT:", left, "RIGHT:",
    #               right, "HIT", dart >= left, "TOTAL", total)
    #         return key
    #     # print("WORD:", key, "LEFT:", left, "RIGHT:",
    #     #       right, "HIT", dart >= left and dart < right)
    #     # if dart >= left and dart < right:
    #     #     word = key

    if isinstance(histogram, list):
        for word_and_count in histogram:
            left = total
            right = total + word_and_count[1]
            total = right
            dart = random.randint(0, total)
            if dart >= left and dart < right:
                return word_and_count[0]


def test_sample_with_histogram(histogram, runs=1000000):
    samples = []
    for i in range(runs):
        word = sampler(histogram)
        samples.append(word)

    if isinstance(histogram, list):
        return listogram(samples)

    if isinstance(histogram, dict):
        return dictogram(samples)


if __name__ == '__main__':
    source_text = get_argument(1, 'data/fish.txt')

    listo = listogram(source_text)
    sample_word = sampler(listo)
    print('LISTOGRAM SAMPLE:', sample_word)

    # dicto = dictogram(source_text)
    # sample_word = sampler(dicto)
    # sample_dictogram = test_sample_with_histogram(dicto, runs=1)
    # print(sample_dictogram)

    # dicto = dictogram(source_text)
    # sample_word = sampler(dicto)
    # print('DICTOGRAM SAMPLE:', sample_word)
