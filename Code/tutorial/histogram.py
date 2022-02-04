"""
Tweet Generator: Analyze Word Frequency in Text

❯ python3 sample.py data/fish.txt
{'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
"""
import sys
import re
import string


def remove_punctuation(str):
    """Removes newlines and punctuation from a string."""
    text = str.lower().replace('\n', ' ').rstrip()
    text_without_punctuation = ''.join(
        [i for i in text if i not in string.punctuation])
    cleaned_text = re.sub(r'[^\w\s]', '', text_without_punctuation)
    return cleaned_text


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


def unique_words(histogram):
    """Returns the total count of unique words in the histogram."""
    histogram = dictogram(source_text)
    return len(histogram.items())


def search(word, listogram):
    """Look for a word in a listogram. Return None if not found."""
    for index, word_and_count in enumerate(listogram):
        if word_and_count[0] == word:
            return word_and_count
    return None


def dictogram(source_text):
    """Return a histogram data structure that stores each unique word along with the number of times the word appears in the source text."""
    word_list = read_file(source_text)
    dictogram = {}
    for word in word_list:
        word_count = dictogram.get(word, 0) + 1
        dictogram[word] = word_count
    return dictogram


def listogram(source_text):
    """Return a histogram data structure that stores each unique word along with the number of times the word appears in the source text."""
    word_list = read_file(source_text)
    unique_words = list(set(word_list))
    listogram = [[word, 0] for word in unique_words]
    for current_word in word_list:
        word_and_count = search(current_word, listogram)
        if word_and_count:
            word_and_count[1] += 1
    return listogram


def frequency(word, histogram):
    """Returns the number of times that `word` appears in a text."""
    if isinstance(histogram, list):
        word_and_count = search(word, histogram)
        if word_and_count:
            return word_and_count[1]
    if isinstance(histogram, dict):
        if word in histogram:
            return histogram[word]
    return 0


def get_argument(index, default):
    """Returns the requested CLI argument, or a sane default."""
    return default if len(sys.argv) <= index else sys.argv[index]


if __name__ == '__main__':
    source_text = get_argument(1, 'data/fish.txt')
    word_to_find = get_argument(2, 'fish')

    dicto = dictogram(source_text)
    word_count_dicto = unique_words(dicto)
    dicto_freq = frequency(word_to_find, dicto)

    listo = listogram(source_text)
    word_count_listo = unique_words(listo)
    listo_freq = frequency(word_to_find, listo)

    print("-" * 60)
    print("Dictogram\tunique_words\t\t", word_count_dicto)
    print("Dictogram\tfrequency of '" + word_to_find + "'\t", dicto_freq)
    print(dicto)
    print("-" * 60)
    print("Listogram\tunique_words\t\t", word_count_listo)
    print("Listogram\tfrequency of '" + word_to_find + "'\t", listo_freq)
    print("-" * 60)
    print(listo)
