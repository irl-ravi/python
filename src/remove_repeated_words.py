# remove_repeated_words.py
import re

def remove_repeated_words(input_text):
    return ' '.join(sorted(set(re.findall(r'\b\w+\b', input_text)), key=lambda x: input_text.index(x)))
