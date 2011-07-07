#!/usr/bin/env python
import sys
import nltk

def get_parts(text):
    text = nltk.word_tokenize(text)
    parts = nltk.pos_tag(text)
    dic = {}
    for work, part in parts:
        if part in dic:
            dic[part].append(work)
        else:
            dic[part] = [work]
    return dic

if __name__ == '__main__':
    print get_parts(sys.argv[1])

