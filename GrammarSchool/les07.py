#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:34:29 2018

@author: huub
"""

derivs = []

class Deriv:
    
    def __init__(self, char):
        self.dvAdditive = None
        self.dvMultitive = None
        self.dvPrimary = None
        self.dvDecimal = None
        self.char = char
    
    def succ(self):
        ident = derivs.index(self)
        return derivs[ident+1]
    
class Result:
    
    def __init__(self, result, next_deriv):
        self.result = result
        self.continuation_deriv = next_deriv

def pAdditive(deriv):
    if deriv.dvAdditive:
        return deriv.dvAdditive
    # First alternative of the grammar
    multitive = pMultitive(deriv)
    if multitive:
        continue_deriv = multitive.continuation_deriv
        if check_initial_char(continue_deriv, '+'):
            additive = pAdditive(continue_deriv.succ())
            if additive:
                n = multitive.result + additive.result
                result = Result(n, additive.continuation_deriv)
                deriv.dvAdditive = result
                return result
    # Second alternative
    deriv.dvAdditive = multitive
    return multitive

def pMultitive(deriv):
    if deriv.dvMultitive:
        return deriv.dvMultitive
    # First alternative of the grammar
    primary = pPrimary(deriv)
    if primary:
        continue_deriv = primary.continuation_deriv
        if check_initial_char(continue_deriv, '*'):
            multitive = pMultitive(continue_deriv.succ())
            if multitive:
                n = primary.result * multitive.result
                result = Result(n, multitive.continuation_deriv)
                deriv.dvMultitive = result
                return result
    # Second alternative
    deriv.dvMultitive = primary
    return primary

def pPrimary(deriv):
    if deriv.dvPrimary:
        return deriv.dvPrimary
    # First alternative of the grammar
    if check_initial_char(deriv, '('):
        additive = pAdditive(deriv.succ())
        if additive:
            if check_initial_char(additive.continuation_deriv, ')'):
                result = Result(additive.result, additive.continuation_deriv.succ())
                deriv.dvPrimary = result
                return result
    # Second alternative
    decimal = pDecimal(deriv)
    deriv.dvPrimary = decimal
    return decimal

def pDecimal(deriv):
    if deriv.dvDecimal:
        return deriv.pDecimal
    if deriv.char == '':
        #print('Expected 0..9 but found nothing')
        return None
    elif deriv.char in ['0','1','2','3','4','5','6','7','8','9']:
        result = Result(int(deriv.char), deriv.succ())
        deriv.dvDecimal = result
        return result
    else:
        #print('Expected 0..9 but found', text[0])
        return None

def check_initial_char(deriv, char):
    return deriv.char != None and deriv.char == char

def parse(text):
    global derivs
    derivs = [0] * (len(text) + 1)
    i = 0
    for char in text:
        derivs[i] = Deriv(char)
        i += 1
    derivs[len(text)] = Deriv(None)
    pAdditive(derivs[0])
    return derivs

text = '(5+4*3)*9'
derivs = parse(text)
print(text, '=', derivs[0].dvAdditive.result)

