import re
import collections

def sentence_counter(text: str):
    new_text = re.sub(r'[.!?][^.!?]', r'||', text)
    return len(new_text.split('||'))

def non_declarative_counter(text: str):
    text = text + '\0'
    pattern = r'[!?][^!?]'
    return len(re.findall(pattern, text))
