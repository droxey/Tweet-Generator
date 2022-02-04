"""
Tweet Generator: Random Dictionary Words
"""

import sys
import random


def rearrange(words):
    """Returns the same words, but all mixed up."""
    random.shuffle(words)
    return words


if __name__ == '__main__':
    unshuffled = sys.argv[1:]
    shuffled = rearrange(sys.argv[1:])
    print(' '.join(shuffled))
