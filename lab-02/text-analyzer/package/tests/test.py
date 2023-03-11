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
	

class TestAverageLengthOfWords(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_word_len('Another sentence.'), 7.5)

    def test_2(self):
        self.assertEqual(count_word_len('My strange sentence.'), 17/3)

    def test_3(self):
        self.assertEqual(count_word_len(''), 0)

    def test_4(self):
        self.assertEqual(count_word_len('Hello!'), 5)

    def test_5(self):
        self.assertEqual(count_word_len('M'), 1)




class TestAmountOfNonDeclarative(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_non_declarative('Hello Mr. Maks! Im a driver.'), 1)

    def test_2(self):
        self.assertEqual(count_non_declarative('H!'), 1)

    def test_3(self):
        self.assertEqual(count_non_declarative(''), 0)

    def test_4(self):
        self.assertEqual(count_non_declarative('I.'), 0)

    def test_5(self):
        self.assertEqual(count_non_declarative('Hello!!!!!!!'), 1)


class TestAverageLengthOfSentence(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_average_chars('Hello Mr. Maks! Im a driver.'), 10)

    def test_2(self):
        self.assertEqual(count_average_chars('Hello!'), 5)

    def test_3(self):
        self.assertEqual(count_average_chars(''), 0)

    def test_4(self):
        self.assertEqual(count_average_chars('1.'), 0)

    def test_5(self):
        self.assertEqual(count_average_chars(' '), 0)

if __name__ == "__main__":
    unittest.main()