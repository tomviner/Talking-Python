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
            return "Why do you like %s?" % random.choice(parts['NN'])

    def response_nouns1(parts):
        if 'NNS' in parts:
            return "Tell me how %s make you feel?" % random.choice(parts['NNS'])

    def response_verb1(parts):
        if 'VB' in parts:
            verb = random.choice(parts['VB'])
            day = random.choice('Mondays Wednesdays Toast Acid'.split())
            return "Wow, I love to %s too, especially on %s. When do you like to %s?" % (verb, day, verb)
        else: return "That's kind of dull. Tell me about your Mother?"            

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
