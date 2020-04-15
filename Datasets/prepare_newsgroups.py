from __future__ import print_function

import io
import os
import sys
import random
from keras.preprocessing.text import Tokenizer

# prepare 20 newsgroups data for a smoother loading
# the loading and normalization approach is taken from:
# https://blog.keras.io/using-pre-trained-word-embeddings-in-a-keras-model.html
BASE_DIR = ''
TEXT_DATA_DIR = os.path.join(BASE_DIR, '20_newsgroup')
MAX_SEQUENCE_LENGTH = 2000


# prepare text samples and their labels
texts = []  # list of text samples
labels_index = {}  # dictionary mapping label name to numeric id
labels = []  # list of label ids
for name in sorted(os.listdir(TEXT_DATA_DIR)):
    path = os.path.join(TEXT_DATA_DIR, name)
    if os.path.isdir(path):
        label_id = unicode(path.split('/')[-1])
        labels_index[name] = label_id
        for fname in sorted(os.listdir(path)):
            if fname.isdigit():
                fpath = os.path.join(path, fname)
                with io.open(fpath, 'r', encoding='latin-1') as f:
                    t = unicode(f.read())
                    i = t.find('\n\n')  # skip header
                    if 0 < i:
                        t = t[i:]
                    texts.append(t)
                labels.append(label_id)

print('Found %s texts.' % len(texts))

# process the dataset as in the Keras tutorial, removing the same punctuation
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# create the simplified dataset with just labels and text snippets
word_index = tokenizer.word_index
inv_words = {v: k for (k, v) in word_index.items()}
parses = [u' '.join([inv_words[w] for w in s][:MAX_SEQUENCE_LENGTH]) for s in sequences]

# dump the dataset
with io.open('20news_simplified.tsv', 'w', encoding='utf8') as f:
    f.write(u'label\tcontent\n')
    full_str = u'\n'.join([u'\t'.join(t) for t in zip(labels, parses)])
    f.write(full_str)

