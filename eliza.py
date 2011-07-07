#!/usr/bin/env python

import sys
import random
from parse import get_parts

PROMPT = '> '
INITIAL_PROMPT = 'How are you feeling?'

def response(s):
    STOCK = ["Hello, what's your favorite animal?"]
    return random.choice(STOCK)

def response2(s):
    parts = get_parts(s)
    if 'NN' in parts:
        return "Why do you like %s?" % random.choice(parts['NN'])
    else:
        return response(s)
        
output = INITIAL_PROMPT
while(True):
    input = raw_input(PROMPT + output + "\n")
    output = response2(input)

