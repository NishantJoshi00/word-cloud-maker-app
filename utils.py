test = "The engineer went into the garden and found the cats lying beneath the trees"

from textblob import TextBlob
from collections import Counter
from nltk.corpus import stopwords
from string import punctuation
def get_words(text):
    processor = TextBlob(text)
    words_count = Counter((word.correct().stem() for word in processor.words))

    return words_count

def remove_stopwords(counter):
    return {key: value for key, value in counter.items() if key not in stopwords.words() and key not in punctuation}
