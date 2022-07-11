test = "The engineer went into the garden and found the cats lying beneath the trees"

from textblob import TextBlob
from collections import Counter
from nltk.corpus import stopwords

def get_words(text):
    processor = TextBlob(text)
    words_count = Counter((TextBlob(word.correct().stem()).correct().raw for word in processor.words))

    return words_count

def remove_stopwords(counter):
    return {key: value for key, value in counter.items() if not key in stopwords.words()}
