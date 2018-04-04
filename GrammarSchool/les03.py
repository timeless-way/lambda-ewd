#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:13:44 2018

@author: huub

Create a python module for the parser and use that to parse expressions.

Run tatsu --outfile calcparser.py grammar1.tatsu in a terminal to 
generate the parser.

Alternatively, use hvtools.generate_parser(basename) which has a similar effect
from the previous lesson to generate the parser directly from python.
See also hvtools.generate_parser(basename)
"""

from hvtools import read_file
import grammar1_parser as gram1 # Generated using hvtools.generate_parser(basename)
import tatsu
import pprint

EXPRESSION_1 = '1 + 2 + 3 + 4'
EXPRESSION_2 = '1*(3+4)'

parser_1 = gram1.Grammar1Parser()

ast = parser_1.parse(EXPRESSION_1)
pprint.pprint(ast, indent=2, width=20)
print(ast)
print()

ast = parser_1.parse(EXPRESSION_2)
pprint.pprint(ast, indent=2, width=20)
print(ast)
print()

GRAMMAR = read_file('grammar1.tatsu')
parser_2 = tatsu.compile(GRAMMAR)

ast = parser_2.parse(EXPRESSION_1)
pprint.pprint(ast, indent=2, width=20)
print(ast)
print()

ast = parser_2.parse(EXPRESSION_2)
pprint.pprint(ast, indent=2, width=20)
print(ast)
print()

