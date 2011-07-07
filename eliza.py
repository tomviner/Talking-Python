#!/usr/bin/env python

import sys
import random
from parse import get_parts

PROMPT = '> '
INITIAL_PROMPT = 'How are you feeling?'

class Responses:
    def response_stock(parts):
        return "How do you feel about that" 

    def response_noun1(parts):
        if 'NN' in parts:
            return "Why do you like %ss?" % random.choice(parts['NN'])

    def response_nouns1(parts):
        if 'NNS' in parts:
            return "Tell me how %s make you feel?" % random.choice(parts['NNS'])

output = INITIAL_PROMPT
while True:
    input = raw_input(PROMPT + output + "\n")
    parts = get_parts(input)
    funcs = [f for (n, f) in Responses.__dict__.items() if callable(f)]
    while True:
        resp = random.choice(funcs)
        funcs.remove(resp)
        output = resp(parts)
        if output:
            break
