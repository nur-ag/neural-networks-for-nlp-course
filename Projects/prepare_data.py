'''Stack Exchange multi-label document classification script

Preprocesses a 'Posts.xml' coming from StackExchange, which can be found:

    https://archive.org/details/stackexchange

For any of the subsites. 

In our particular case, we preprocess the cooking stack exchange.
'''
import html2text
import regex as re
from xml.dom import minidom

import io
from collections import Counter

TAGS_TO_KEEP = 300


h = html2text.HTML2Text()
h.ignore_links = True


def preprocess_body(body):
    '''Preprocess the body of a post.

    The preprocessing pipeline is:
      1. removing html tags
      2. removing punctuation
      3. removing repeated whitespace
      4. lowercasing
      5. trimming both ends of the string'''
    plaintext_body = h.handle(body)
    no_puncts_body = re.sub(ur'\p{P}+', u' ', plaintext_body)
    no_rep_ws_body = re.sub(ur'\s+', u' ', no_puncts_body)
    lowercase_body = no_rep_ws_body.lower()
    return lowercase_body.strip()


def preprocess_tags(tags):
    '''Preprocess the tags of a post.

    Takes a list of tags in the form:

      `<tag1><tag2><tag3>...<tagN>`

    and produces an N element list, filtering out the empty tag.
    '''
    tags_splitter = tags.replace(u'><', u'>|<')
    tags_nomarker = tags_splitter.replace(u'>', u'').replace(u'<', u'')
    tags_list = tags_nomarker.split(u'|')
    return [t for t in tags_list if t]


def preprocess_row(row):
    '''Preprocesses a whole post.

    Applies body and tag preprocessing to the post.'''
    body = preprocess_body(row.getAttribute('Body'))
    tags = preprocess_tags(row.getAttribute('Tags'))
    return body, tags


# read all the posts in the stack overflow sub-site
doc = minidom.parse('Posts.xml')
entries = [preprocess_row(r) for r in doc.getElementsByTagName('row')]

# compute all tags, and keep only posts that are tagged
all_tags = Counter(l for e in entries for l in e[1])
most_common_tags = all_tags.most_common(TAGS_TO_KEEP)
tag_indices = {t[0]: i for i, t in enumerate(most_common_tags)}
tagged_entries = [e for e in entries if e[1] and any(t in tag_indices for t in e[1])]

# dump the multilabel dataset
with io.open('se_cooking.tsv', 'w', encoding='utf8') as f:
    for (body, tags) in tagged_entries:
        tags_to_print = sorted([t for t in tags if t in tag_indices])
        tags_formatted = u'|'.join(tags_to_print)
        f.write(u'{}\t{}\n'.format(tags_formatted, body))
