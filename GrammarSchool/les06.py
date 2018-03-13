#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:08:00 2018

@author: huub
"""
full_backtrack = True

class Deriv:
    
    def __init__(self, text):
        self.dvAdditive = None
        self.dvMultitive = None
        self.dvPrimary = None
        self.dvDecimal = None
        if len(text) > 0:
            self.dvChar = Result(text[0], Deriv(text[1:]))
        else:
            self.dvChar = Result('', None)
    
class Result:
    
    def __init__(self, result, next_deriv):
        self.result = result
        self.next_deriv = next_deriv

def pAdditive(deriv):
    if deriv.dvAdditive:
        return deriv.dvAdditive
    # First alternative of the grammar
    multitive = pMultitive(deriv)
    if multitive:
        rest = multitive.next_deriv
        if check_initial_char(rest, '+'):
            res = pAdditive(rest.dvChar.next_deriv)
            if res:
                n = multitive.result + res.result
                result = Result(n, res.next_deriv)
                deriv.dvAdditive = result
                return result
    # Second alternative
    if full_backtrack:
        multitive = pMultitive(deriv) # Do this again for backtracking!
    deriv.dvAdditive = multitive
    return multitive

def pMultitive(deriv):
    if deriv.dvMultitive:
        return deriv.dvMultitive
    # First alternative of the grammar
    primary = pPrimary(deriv)
    if primary:
        rest = primary.next_deriv
        if check_initial_char(rest, '*'):
            res = pMultitive(rest.dvChar.next_deriv)
            if res:
                n = primary.result * res.result
                result = Result(n, res.next_deriv)
                deriv.dvMultitive = result
                return result
    # Second alternative
    if full_backtrack:
        primary = pPrimary(deriv) # Do this again for backtracking!
    deriv.dvMultitive = primary
    return primary

def pPrimary(deriv):
    if deriv.dvPrimary:
        return deriv.dvPrimary
    # First alternative of the grammar
    if check_initial_char(deriv, '('):
        additive = pAdditive(deriv.dvChar.next_deriv)
        if additive:
            if check_initial_char(additive.next_deriv, ')'):
                result = Result(additive.result, additive.next_deriv.dvChar.next_deriv)
                deriv.dvPrimary = result
                return result
    # Second alternative
    decimal = pDecimal(deriv)
    deriv.dvPrimary = decimal
    return decimal

def pDecimal(deriv):
    if deriv.dvDecimal:
        return deriv.pDecimal
    if deriv.dvChar.result == '':
        #print('Expected 0..9 but found nothing')
        return None
    elif deriv.dvChar.result in ['0','1','2','3','4','5','6','7','8','9']:
        result = Result(int(deriv.dvChar.result), deriv.dvChar.next_deriv)
        deriv.dvDecimal = result
        return result
    else:
        #print('Expected 0..9 but found', text[0])
        return None

def check_initial_char(deriv, char):
    return deriv.dvChar != None and deriv.dvChar.result == char

def parse(text):
    derivs = Deriv(text)
    return pAdditive(derivs)

text = '(5+4)*(3+4)'
derivs = parse(text)
print(text, '=', derivs.result)

