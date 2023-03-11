from package.source.functions import count_sentences
from package.source.functions import count_non_declarative
from package.source.functions import count_average_chars
from package.source.functions import count_word_len
from package.source.functions import count_ngrams_top

def main():
    text = input()
    print('Amount of sentences in the text: ' + str(count_sentences(text)))
    print('Amount of non-declarative sentences in the text: ' + str(count_non_declarative(text)))
    try:
        print('Average length of the sentence in characters (words count only): ' + str(count_average_chars(text)))
        print('Average length of the word in the text in characters: ' + str(count_word_len(text)))
    except ZeroDivisionError:
        print('No sentence has been inputed!')
    try:
        k = int(input('Enter how long should be top of most repeated N-grams: '))
        n = int(input('Enter the length of N-gram: '))
        count_ngrams_top(text, k, n)
    except ValueError:
        print('Incorrect Input!')


if __name__ == '__main__':
    main()