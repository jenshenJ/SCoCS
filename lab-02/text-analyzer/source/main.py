from functions import sentence_counter
from functions import non_declarative_counter
from functions import average_chars_counter
from functions import word_len_counter
from functions import top_counter

text = input()
print('Amount of sentences in the text: ' + str(sentence_counter(text)))
print('Amount of non-declarative sentences in the text: ' + str(non_declarative_counter(text)))
try:
    print('Average length of the sentence in characters (words count only): ' + str(average_chars_counter(text)))
    print('Average length of the word in the text in characters: ' + str(word_len_counter(text)))
except ZeroDivisionError:
    print('No sentence has been inputed!')
try:
    k = int(input('Enter how long should be top of most repeated N-grams(0 for default): '))
    n = int(input('Enter the length of N-gram(0 for default): '))
    top_counter(text, k, n)
except ValueError:
    print('Incorrect Input!')