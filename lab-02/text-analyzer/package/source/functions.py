import re
from ..source.abbreviations import SINGLE_ABREBIATIONS, DOUBLE_ABREVIATIONS
from collections import Counter

def count_sentences(text: str):
    new_text = re.sub(r"[.!?][^.!?]", r"||", text)
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
    pattern = r"[!?][^!?]"

    return len(re.findall(pattern, text))


def count_average_chars(text: str):
    sentence_count = count_sentences(text)
    new_text = text.lower()                             # ignore register
    new_text = re.sub(
        r"\b[0-9]+\b\s*", "", new_text
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
        r"\b[0-9]+\b\s*", "", text
    )                                                   # deleting from text words with numbers only
    word_count = len(re.findall(r"\w+", new_text))
    new_text = "".join(
        ch for ch in new_text if ch.isalnum()
    )                                                   # deleting al non-alphabet-numeric symbols
    if word_count == 0:
        return 0
      
    return len(new_text) / word_count


def ngrams(text: str, n: int):
    return [text[i:i + n] for i in range(len(text) - n + 1)]


def count_ngrams_top(text: str, k: int = 10, n: int = 4):
    text_ngrams = ngrams(text, n)
    counter = Counter(text_ngrams)
    k_items = counter.most_common(k)

    for ngram, count in k_items:
        print(f'"{ngram}" repeates {count} time{"s" if count != 1 else ""}')
    