#!/usr/bin/env python

import sys

PROMPT = '> '
INITIAL_PROMPT = 'How are you feeling?'

def response(s):
  return "Hello, what's your name?"

output = INITIAL_PROMPT
while(True):
  input = raw_input(PROMPT + output + "\n")
  output = response(input)

