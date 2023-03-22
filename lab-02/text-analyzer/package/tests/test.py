import unittest

from ..source.functions import (
    count_sentences,
    count_non_declarative,
    count_average_chars,
    count_word_len,
    print_ngrams_top
)

class TestCountSentences(unittest.TestCase):
    
    def test_1(self):
        EXCEPTED_VALUE = 1
        RETURNED_VALUE = count_sentences('Hello, World!')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)
        
    def test_2(self):
        EXCEPTED_VALUE = 1
        RETURNED_VALUE = count_sentences('Hello, World.')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)
        
    def test_3(self):
        EXCEPTED_VALUE = 1
        RETURNED_VALUE = count_sentences('Are you okey?')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)
        
    def test_4(self):
        EXCEPTED_VALUE = 1
        RETURNED_VALUE = count_sentences('Hello, Mrs.Marple...')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)
        
    def test_5(self):
        EXCEPTED_VALUE = 3
        RETURNED_VALUE = count_sentences('There is some great news when it comes to job interviews. It’s not all '
                                         'doom and gloom (bad). Most recruiters these days ask the interviewees ('
                                         'you) the same basic questions.')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)
        
    def test_6(self):
        EXCEPTED_VALUE = 2
        RETURNED_VALUE = count_sentences('Wtf?! I don\'t want know what u feeling.')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)
	

class TestAverageLengthOfWords(unittest.TestCase):
    def test_1(self):
        EXCEPTED_VALUE = 7.5
        RETURNED_VALUE = count_word_len('Another sentence.')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)

    def test_2(self):
        EXCEPTED_VALUE = 17/3
        RETURNED_VALUE = count_word_len('Mt strange sentence.')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)


    def test_3(self):
        EXCEPTED_VALUE = 0
        RETURNED_VALUE = count_word_len('')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)
    

    def test_4(self):
        EXCEPTED_VALUE = 5
        RETURNED_VALUE = count_word_len('Hello!!')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)
        

    def test_5(self):
        EXCEPTED_VALUE = 1
        RETURNED_VALUE = count_word_len('M')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)


class TestAmountOfNonDeclarative(unittest.TestCase):
    def test_1(self):
        EXCEPTED_VALUE = 1
        RETURNED_VALUE = count_non_declarative('Hello Mr. Maks! Im a driver.')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)

    def test_2(self):
        EXCEPTED_VALUE = 1
        RETURNED_VALUE = count_non_declarative('Hi!')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)


    def test_3(self):
        EXCEPTED_VALUE = 0
        RETURNED_VALUE = count_non_declarative('')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)


    def test_4(self):
        EXCEPTED_VALUE = 0
        RETURNED_VALUE = count_non_declarative('I.')
        self.assertEqual(RETURNED_VALUE, EXCEPTED_VALUE)
        
    def test_5(self):
        EXCEPTED_VALUE = 1
        RETURNED_VALUE = count_non_declarative('Hello!!!!!')
        self.assertEqual(EXCEPTED_VALUE, RETURNED_VALUE)


class TestAverageLengthOfSentence(unittest.TestCase):
    def test_1(self):
        EXCEPTED_VALUE = 10
        RETURNED_VALUE = count_average_chars('Hello Mr. Maks! Im a driver.')
        self.assertEqual(EXCEPTED_VALUE, RETURNED_VALUE)


    def test_2(self):
        EXCEPTED_VALUE = 5
        RETURNED_VALUE = count_average_chars('Hello Mr. Maks! Im a driver.')
        self.assertEqual(EXCEPTED_VALUE, RETURNED_VALUE)
        self.assertEqual(count_average_chars('Hello!'), 5)

    def test_3(self):
        EXCEPTED_VALUE = 0
        RETURNED_VALUE = count_average_chars('')
        self.assertEqual(EXCEPTED_VALUE, RETURNED_VALUE)

    def test_4(self):
        EXCEPTED_VALUE = 0
        RETURNED_VALUE = count_average_chars('1.')
        self.assertEqual(EXCEPTED_VALUE, RETURNED_VALUE)

    def test_5(self):
        EXCEPTED_VALUE = 0
        RETURNED_VALUE = count_average_chars(' ')
        self.assertEqual(EXCEPTED_VALUE, RETURNED_VALUE)

if __name__ == "__main__":
    unittest.main()