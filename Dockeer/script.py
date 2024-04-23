with open(r'paragraphs.txt')as file :
    lines=file.read()

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("stopwords")

def remove_stopwords(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    filtered_text = ' '.join(filtered_tokens)

    return filtered_text

filtered_text = remove_stopwords(lines)

import re
from nltk import FreqDist
words_list = re.split(r'[ ,.?!\n\(\)\[\]]+', filtered_text)
word_freq = FreqDist(words_list)

for word, frequency in word_freq.items():
    print(f"{word}:{frequency}")