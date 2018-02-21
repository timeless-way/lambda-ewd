#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:13:44 2018

@author: huub

Create a python module for the parser and use that to parse ecpressions.

Use tatsu --outfile calcparser.py grammar1.tatsu in a terminal to 
generate the parser.

Alternatively, use 

p = tatsu.to_python_sourcecode(GRAMMAR)
write_file('<MODULENAME>.py', p)

from the previous lesson to generate teh parser directly from python.
"""

import calcparser as cp # Generated using tatsu in a terminal
import parser as pp     # Generated using to_python_sourcecode

import pprint

EXPRESSION_1 = '1 + 2 + 3 + 4'
EXPRESSION_2 = '1*(3+4)'

parser_1 = cp.CalculatorParser()
parser_2 = pp.CalculatorParser()

ast = parser_1.parse(EXPRESSION_1)
pprint.pprint(ast, indent=2, width=20)
print(ast)

ast = parser_1.parse(EXPRESSION_2)
pprint.pprint(ast, indent=2, width=20)
print(ast)

ast = parser_2.parse(EXPRESSION_1)
pprint.pprint(ast, indent=2, width=20)
print(ast)

ast = parser_2.parse(EXPRESSION_2)
pprint.pprint(ast, indent=2, width=20)
print(ast)
