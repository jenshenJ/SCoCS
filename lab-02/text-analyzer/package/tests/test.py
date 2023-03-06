import unittest

from ..source.functions import (
    count_sentences,
    count_non_declarative,
    count_average_chars,
    count_word_len,
    count_ngrams_top
)

class TestCountSentences(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_sentences('Hello, World!'), 1)
        
    def test_2(self):
        self.assertEqual(count_sentences('Hello, World.'), 1)
        
    def test_3(self):
        self.assertEqual(count_sentences('Are you okey?'), 1)
        
    def test_4(self):
        self.assertEqual(count_sentences('Hello, Mrs.Marple...'), 1)
        
    def test_5(self):
        self.assertEqual(count_sentences('There is some great news when it comes to job interviews. It’s not all '
                                         'doom and gloom (bad). Most recruiters these days ask the interviewees ('
                                         'you) the same basic questions.'), 3)
        
    def test_6(self):
        self.assertEqual(count_sentences('Wtf?! I don\'t want know what u feeling.'), 2)
	

if __name__ == "__main__":
    unittest.main()