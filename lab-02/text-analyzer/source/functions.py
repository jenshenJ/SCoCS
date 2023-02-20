import re
import collections

def sentence_counter(text: str):
    new_text = re.sub(r'[.!?][^.!?]', r'||', text)
    return len(new_text.split('||'))