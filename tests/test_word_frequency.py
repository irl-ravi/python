# test_word_frequency.py
import unittest
from src.word_frequency import compute_word_frequency

class TestWordFrequency(unittest.TestCase):
    def test_compute_word_frequency(self):
        input_text = "which is better python 2 or python 3"
        result = compute_word_frequency(input_text)
        expected_result = [('2', 1), ('3', 1), ('better', 1), ('is', 1), ('or', 1), ('python', 2), ('which', 1)]
        self.assertEqual(result, expected_result)
