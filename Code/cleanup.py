"""
Module for cleaning up source text.
"""
import string
import re

def remove_punctuation(str):
    """Removes newlines and punctuation from a string."""
    text = str.lower().replace('\n', ' ').rstrip()
    text_without_punctuation = ''.join(
        [i for i in text if i not in string.punctuation])
    cleaned_text = re.sub(r'[^\w\s]', '', text_without_punctuation)
    return cleaned_text
