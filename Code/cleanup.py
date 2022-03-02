import json
from tokens import remove_punctuation
import string

if __name__ == '__main__':
    quotes = []
    names = []

    filename = "data/allquotes.json"
    source = open(filename)
    data = json.load(source)

    quotes.append("MARKOVSTART")
    for quote in data:
        if quote.get('Character') == 'Jake':
            quotes.append(quote.get('Line'))
    quotes.append("MARKOVEND")

    all_quotes = " ".join(quotes)
    corpus_file = open("data/corpus.txt", "w")
    corpus_file.write(all_quotes)

    all_names = "\n".join(names)
    names_file = open("data/names.txt", "w")
    names_file.write(all_names)
