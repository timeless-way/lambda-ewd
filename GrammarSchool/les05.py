#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 12:58:03 2018

@author: huub

A recursive descent parser for Ford-2002
Now with Birman-Ullman memoization!

Grammar:
Additve   <- Multitive '+' Additive | Multitive
Multitive <- Primary '*' Multitive | Primary
Primary   <- '(' Additive ')' | Decimal
Decimal   <- 0..9
"""
from les04 import ParserResult, pAdditive, pMultitive, pPrimary, pDecimal, call_count

"""
Set memoize to True to enjoy the benefits of memoization.
Set it to False and you have exactly les04.
"""
memoize = True

"""
If tracing is set to True, a line will be printed for each syntatctic function call.
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
#call_count = 0
memo_table = {}

def p5Additive(text):
    if memoize and memo_table['pAdditive'][text]:
        return memo_table['pAdditive'][text]
    result = pAdditive(text)
    memo_table['pAdditive'][text] = result
    return result

def p5Multitive(text):
    if memoize and memo_table['pMultitive'][text]:
        return memo_table['pMultitive'][text]
    result = pMultitive(text)
    memo_table['pMultitive'][text] = result
    return result

def p5Primary(text):
    if memoize and memo_table['pPrimary'][text]:
        return memo_table['pPrimary'][text]
    result = pPrimary(text)
    memo_table['pPrimary'][text] = result
    return result

def p5Decimal(text):
    if memoize and memo_table['pDecimal'][text]:
        return memo_table['pDecimal'][text]
    result = pPrimary(text)
    memo_table['pDecimal'][text] = result
    return result

def root5(text):
    global call_count
    print(text)
    call_count = 0
    init_table(text)
    res = p5Additive(text)
    if res and len(res.next_text) == 0:
        print('Parse OK:', res.parse_value)
    elif res and len(res.next_text) > 0:
        print('Parse OK, but with remaining text:', res.next_text, 'value:', res.parse_value)
    else:
        print('Parse error')
    print('call count:', call_count)
    print('-----------------------------------------------------------')

def init_table(text):
    global tracing, memo_table
    keys = [text[i:] for i in range(len(text))]
    memo_table = {}
    memo_table['pAdditive'] = {}.fromkeys(keys)
    memo_table['pMultitive'] = {}.fromkeys(keys)
    memo_table['pPrimary'] = {}.fromkeys(keys)
    memo_table['pDecimal'] = {}.fromkeys(keys)

#    tracing = False
#    for text in reversed(keys):
#        p5Additive(text)
#        p5Multitive(text)
#        p5Primary(text)
#        p5Decimal(text)
#    tracing = True
    
def show_table(table):
    row_names = sorted(list(table.keys()))
    col_names = build_col_names(table[row_names[0]])
    text = col_names[0]

    print_table_header(col_names, text)
    for rn in row_names:
        print(rn + ':\t', end='')
        for cn in col_names:
            parse_result = table[rn][cn]
            if parse_result:
                index = str(string_to_index(parse_result.next_text, text))
                value = str(parse_result.parse_value)
                print('<' + value + ',' + index + '>' + '\t', end='')
            else:
                print('-\t', end='')
        print()

def build_col_names(col_dict):
    col_keys = col_dict.keys()
    col_names = [''] * len(col_keys)
    for ck in col_keys:
        col_names[len(ck)-1] = ck
    col_names.reverse()
    return col_names

def print_table_header(col_names, text):
    print()
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('table for ' + text)
    print()
    print('\t'*2, end='')
    for cn in col_names:
        print(string_to_index(cn, text), end='\t')
    print()

def string_to_index(string, text):
    return len(text) - len(string)

def index_to_string(index, text):
    return text[index:]
    

#root5('3+(4*5)+7*(3+1)')
root5('(3*2)*(2+7)')

show_table(memo_table)