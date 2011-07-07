#!/usr/bin/env python

import sys
import random
from parse import get_parts

PROMPT = '> '
INITIAL_PROMPT = 'How are you feeling?'

class Responses:
    def response_stock(parts):
        return random.choice(["How do you feel about that?", "What's your favourite animal?", "Tell me about your mother?"])

    def response_noun1(parts):
        responses = ["Why do you like %s?", "What do you like most about %s?", "Tell me more about %s?"]
        if 'NN' in parts:
            return random.choice(responses) % random.choice(parts['NN'])

    def response_nouns2(parts):
        if 'NN' in parts:
            noun = random.choice(parts['NN'])
            return "%s, %s, %s! Can you talk about something else please!" % (noun, noun.title(), noun.upper())

    def response_nouns1(parts):
        responses = ["Tell me how %s make you feel?"]
        if 'NNS' in parts:
            return random.choice(responses) % random.choice(parts['NNS'])

    def response_verb1(parts):
        if 'VB' in parts:
            verb = random.choice(parts['VB'])
            day = random.choice('Mondays Wednesdays Toast Acid'.split())
            return "Wow, I love to %s too, especially on %s. When do you like to %s?" % (verb, day, verb)

output = INITIAL_PROMPT
while True:
    input = raw_input(PROMPT + output + "\n")
    if input == "goodbye":
        print "Fine...seeyas!"
        sys.exit(0)
    parts = get_parts(input)
    funcs = [f for (n, f) in Responses.__dict__.items() if callable(f)]
    while True:
        resp = random.choice(funcs)
        funcs.remove(resp)
        output = resp(parts)
        if output:
            break
