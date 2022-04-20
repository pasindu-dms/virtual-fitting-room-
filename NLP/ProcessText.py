import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
sample_text = 'blue shirt with white collar'

stop_words = set(stopwords.words('english') + list(string.punctuation))

stop_words_removed = ' '.join([i for i in word_tokenize(sample_text.lower()) if i not in stop_words])

print(stop_words_removed)

pos_tagged = nltk.pos_tag(nltk.word_tokenize(stop_words_removed))

print(pos_tagged)

adjectives = []
nouns = []

for tag in pos_tagged:
    cat = tag[1]
    word = tag[0]
    if cat == 'JJ':
        adjectives.append(word)
    elif cat == 'NN':
        nouns.append(word)

print(adjectives)
print(nouns)