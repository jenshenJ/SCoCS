import re
import collections

def sentence_counter(text: str):
    new_text = re.sub(r'[.!?][^.!?]', r'||', text)
    return len(new_text.split('||'))

def non_declarative_counter(text: str):
    text = text + '\0'
    pattern = r'[!?][^!?]'
    return len(re.findall(pattern, text))


def average_chars_counter(text: str):
    sentence_count = sentence_counter(text)
    new_text = text.lower()                                           #ignore register
    new_text = re.sub(r'\b[0-9]+\b\s*', '', new_text)                 #deleting from text words with numbers only
    new_text = ''.join(ch for ch in new_text if ch.isalnum())         #deleting al non-alphabet-numeric symbols
    return len(new_text) / sentence_count 

