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

"""
if tracing is set to True, a line will be printed for each syntatctic function call.
This line contains the name of the function and the text to be parsed.
WARNING: The output will be overwhelming!
"""
tracing = False

"""
full_backtrack = True -> all strings are reparsed if an alternative failed
full_backtrack = False -> previous resultas are used again (kind of packratting!)
"""
full_backtrack = False

"""
Count the number of calls to syntatctic functions. This is printed at the end 
of the analyis.
WARNING: This gives a feeling for the notion of exponential complexity.
"""
call_count = 0

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
    if full_backtrack:
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
    if full_backtrack:
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
        #print('Expected 0..9 but found nothing')
        return None
    elif text[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return ParserResult(int(text[0]), text[1:])
    else:
        #print('Expected 0..9 but found', text[0])
        return None

def root(text):
    global call_count
    print(text)
    call_count = 0
    res = pAdditive(text)
    if res and len(res.next_text) == 0:
        print('Parse OK:', res.parse_value)
    elif res and len(res.next_text) > 0:
        print('Parse OK, but some text was not parsed:', res.next_text, 'value:', res.parse_value)
    else:
        print('Parse error')
    print('call count:', call_count)
    print('-----------------------------------------------------------')

def check_initial_char(s, c):
    return len(s) > 0 and s[0] == c

tracing = False
def trace(s, exp):
   global tracing, call_count
   call_count += 1
   if tracing:
       print(s, '\t', exp)

#root('1')
#root('1+1')
#root('1+1+1')
#root('1+1+1+1')
#root('1+1+1+1+1')
#root('1+1+1+1+1+1')
#root('1+1+1+1+1+1+1')
#root('1+1+1+1+1+1+1+1')
#root('(1)')
#root('((1))')
#root('(((1)))')
#root('((((1))))')
#root('(((((1)))))')
#root('((((((1))))))')
#
##root('4')
#
#tracing = False
#root('3+6')
#tracing = False
#
#root('3*(4+5)')
#
#tracing = False
#root('(4*5)+7*(3+1)')
#tracing = False
#
#root('3+(4*5)+7*(3+1)')
#root('3*')
#root('(3+5')