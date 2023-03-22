from package.source.functions import count_sentences
from package.source.functions import count_non_declarative
from package.source.functions import count_average_chars
from package.source.functions import count_word_len
from package.source.functions import print_ngrams_top

def main():
    try:
        text = input()
        print('Amount of sentences in the text: ' + str(count_sentences(text)))
        print('Amount of non-declarative sentences in the text: ' + str(count_non_declarative(text)))

        try:
            print('Average length of the sentence in characters (words count only): ' + str(count_average_chars(text)))
            print('Average length of the word in the text in characters: ' + str(count_word_len(text)))

        except ZeroDivisionError:
            print('No sentence has been inputed!')

        try:
            n, k = map(int, input('Enter N and K to get topK repeated N-grams in the text: ').split())
            print_ngrams_top(text, k, n)

        except ValueError:
            print_ngrams_top(text)

    except KeyboardInterrupt :
        print("See you later!")

if __name__ == '__main__':
    main()