import re
import numpy as np



def to_lower(text):
    return text.lower()



def expand_contractions(text):
    text = re.sub(r"won\'t'", "will not", text)
    text = re.sub(r"can\'t'", "can not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    return text



def remove_special_characters(text):
    pattern = r"[^a-zA-Z0-9\s]"
    return re.sub(pattern, "", text)



def remove_empty_words(words):
    return [word.strip() for word in words if word.strip() != ""]