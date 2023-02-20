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

def word_len_counter(text: str):
    new_text = text.lower()                                           #ignore register
    new_text = re.sub(r'\b[0-9]+\b\s*', '', text)                     #deleting from text words with numbers only
    word_count = len(re.findall(r'\w+', new_text))          
    new_text = ''.join(ch for ch in new_text if ch.isalnum())         #deleting al non-alphabet-numeric symbols
    return len(new_text) / word_count

def top_counter(text: str, k: int, n: int):
    substring_dict = collections.defaultdict(int)
    if k == 0:                                                  #setting default values
        k = 10
    if n == 0:
        n = 4

    for i, j in enumerate(text):
        if i + n < len(text):
            substring_dict[text[i:i+n]] += 1
        else:
            break
        
    if len(substring_dict) == 0:
        print('There is no any ', n, '-grams in text')
        return
    else:
        substring_dict = dict(substring_dict)
        sorted_dict = dict(sorted(substring_dict.items(), key=lambda item : item[1], reverse=True))
        sorted_list = list(sorted_dict)
        k = min(len(sorted_list), k)
        for i in range(k):
            print(str(i + 1), '. ', sorted_list[i],' - ' , sorted_dict[sorted_list[i]],sep='')
            

