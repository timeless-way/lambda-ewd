#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 08:26:36 2018

@author: huub
"""

import pprint
from tatsu import parse
from hvtools import read_file

def main():
    GRAMMAR = read_file('grammar1.tatsu')
    print('Grammar:', GRAMMAR)
    EXPRESSION = '1 + 2 + 3 + 4'
    ast = parse(GRAMMAR, EXPRESSION)
    print('PPRINT')
    pprint.pprint(ast, indent=2, width=20)
    print('Type ast', type(ast))
    print('Expr', EXPRESSION)
    print('Not pretty', ast)
    
main()