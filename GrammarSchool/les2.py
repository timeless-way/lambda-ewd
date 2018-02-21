#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:54:19 2018

@author: huub
Create a parser object so several expressions can be parsed by the same parser.
"""

import tatsu
from hvtools import generate_parser

GRAMMAR = read_file('grammar1.tatsu')
EXPRESSION_1 = '1 + 2 + 3 + 4'
EXPRESSION_2 = '1*(3+4)'

parser = tatsu.compile(GRAMMAR)
#ast = parser.parse(EXPRESSION_1)
#pprint.pprint(ast, indent=2, width=20)
#
#ast = parser.parse(EXPRESSION_2)
#pprint.pprint(ast, indent=2, width=20)

#p = tatsu.to_python_sourcecode(GRAMMAR)
#write_file('parser.py', p)

generate_parser('grammar1')