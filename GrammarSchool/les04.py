#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 12:58:03 2018

@author: huub

A recursive descent parser for Ford-2002

Grammar:
Additve   <- Multitive '+' Additive | Multitive
Multitive <- Primary '*' Multitive | Primary
Primary   <- '(' Additive ')' | Decimal
Decimal   <- 0..9
"""

class ParserResult:
    
    def __init__(self, result, rest):
        self.next_text = rest
        self.parse_value = result

def pAdditive(text):
    # First alternative of the grammar
    trace('pAdditive 1', text)
    multitive = pMultitive(text)
    if multitive:
        rest = multitive.next_text
        if check_initial_char(rest, '+'):
            res = pAdditive(rest[1:])
            if res:
                n = multitive.parse_value + res.parse_value
                return ParserResult(n, res.next_text)
    # Second alternative
    trace('pAdditive 2', text)
    multitive = pMultitive(text) # Do this again for backtracking!
    return multitive

def pMultitive(text):
    # First alternative of the grammar
    trace('pMultitative 1', text)
    primary = pPrimary(text)
    if primary:
        rest = primary.next_text
        if check_initial_char(rest, '*'):
            res = pMultitive(rest[1:])
            if res:
                n = primary.parse_value * res.parse_value
                return ParserResult(n, res.next_text)
    # Second alternative
    trace('pMultitative 2', text)
    primary = pPrimary(text) # Do this again for backtracking!
    return primary

def pPrimary(text):
    # First alternative of the grammar
    trace('pPrimary 1', text)
    if check_initial_char(text, '('):
        additive = pAdditive(text[1:])
        if additive:
            if check_initial_char(additive.next_text, ')'):
                return ParserResult(additive.parse_value, additive.next_text[1:])
    # Second alternative
    trace('pPrimary 2', text)
    decimal = pDecimal(text)
    return decimal

def pDecimal(text):
    trace('pDecimal', text)
    if len(text) == 0:
        print('Expected 0..9 but found nothing')
        return None
    elif text[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return ParserResult(int(text[0]), text[1:])
    else:
        print('Expected 0..9 but found', text[0])
        return None

def root(text):
    print(text)
    res = pAdditive(text)
    if res and len(res.next_text) == 0:
        print('Parse OK:', res.parse_value)
    elif res and len(res.next_text) > 0:
        print('Parse OK, but some text was not parsed:', res.next_text)
    else:
        print('Parse error')
    print('-----------------------------------------------------------')

def check_initial_char(s, c):
    return len(s) > 0 and s[0] == c

tracing = False
def trace(s, exp):
   global tracing
   if tracing:
       print(s, '\t', exp)

root('4')

tracing = True
root('3+6')
tracing = False

root('3*(4+5)')
tracing = False
root('(4*5)+7*(3+1)')
tracing = False
root('3+(4*5)+7*(3+1)')
root('3*')
root('(3+5')