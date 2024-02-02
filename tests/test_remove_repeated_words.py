# test_remove_repeated_words.py
import unittest
from src.remove_repeated_words import remove_repeated_words

class TestRemoveRepeatedWords(unittest.TestCase):
    def test_remove_repeated_words(self):
        input_text = "Hello Hello World"
        result = remove_repeated_words(input_text)
        expected_result = "Hello World"
        self.assertEqual(result, expected_result)
