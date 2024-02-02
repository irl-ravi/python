# word_frequency.py
from collections import Counter

def compute_word_frequency(input_text):
    words = input_text.split()
    frequency = Counter(words)
    sorted_frequency = sorted(frequency.items())
    return sorted_frequency

