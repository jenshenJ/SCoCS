import re
from ..source.abbreviations import SINGLE_ABREBIATIONS, DOUBLE_ABREVIATIONS
from collections import defaultdict


#Regular expressions
SENTENCE_PATTERN = r"[.!?][^.!?]"
NONDECLARATIVE_PATTERN = r"[!?][^!?]"
ONLY_NUMBERS_PATTERN = r"\b[0-9]+\b\s*"

def count_sentences(text: str):
    new_text = re.sub(SENTENCE_PATTERN, r"||", text)
    sentence_number = len(new_text.split("||"))

    for abbr in SINGLE_ABREBIATIONS:
        if text.find(abbr) != -1:
            sentence_number -= 1
            
    for abbr in DOUBLE_ABREVIATIONS:
        if text.find(abbr) != -1:
            sentence_number -= 2

    return sentence_number


def count_non_declarative(text: str):
    text = text + "\0"
    pattern = NONDECLARATIVE_PATTERN

    return len(re.findall(pattern, text))


def count_average_chars(text: str):
    sentence_count = count_sentences(text)
    new_text = text.lower()                             # ignore register
    new_text = re.sub(
        ONLY_NUMBERS_PATTERN, "", new_text
    )                                                   # deleting from text words with numbers only
    new_text = "".join(
        ch for ch in new_text if ch.isalnum()
    )                                                   # deleting al non-alphabet-numeric symbols
    
    if sentence_count == 0:
        return 0
    
    return len(new_text) / sentence_count


def count_word_len(text: str):
    new_text = text.lower()                             # ignore register
    new_text = re.sub(
        ONLY_NUMBERS_PATTERN, "", text
    )                                                   # deleting from text words with numbers only
    word_count = len(re.findall(r"\w+", new_text))
    new_text = "".join(
        ch for ch in new_text if ch.isalnum()
    )                                                   # deleting al non-alphabet-numeric symbols
    if word_count == 0:
        return 0
      
    return len(new_text) / word_count


def generate_ngrams(text: str, n: int):
    return [text[i:i + n] for i in range(len(text) - n + 1)]



def print_ngrams_top(text: str, k: int = 10, n: int = 4):
    substring_dict = defaultdict(int)
    ngrams = generate_ngrams(text, n)
    for ngram in ngrams:
        substring_dict[ngram] += 1
   
    if len(substring_dict) == 0:
        print('There is no any ', n, '-grams in text')
        return
    
    else:
        substring_dict = dict(substring_dict)
        sorted_dict = dict(sorted(substring_dict.items(), key=lambda item :item[1] , reverse=True))
        sorted_list = list(sorted_dict)
        k = min(len(sorted_list), k)

        for i in range(k):
            count = sorted_dict[sorted_list[i]]
            print(f'{str(i + 1)}. {sorted_list[i]} - {count} time{"s" if count != 1 else ""}')