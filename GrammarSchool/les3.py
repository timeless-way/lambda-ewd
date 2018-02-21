#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:13:44 2018

@author: huub

Create a python module for the parser and use that to parse ecpressions.

Use tatsu --outfile calcparser.py grammar1.tatsu in a terminal to 
generate the parser.
"""

import calcparser as cp
import pprint

EXPRESSION_1 = '1 + 2 + 3 + 4'
EXPRESSION_2 = '1*(3+4)'

parser = cp.CalculatorParser()
ast = parser.parse(EXPRESSION_2)
pprint.pprint(ast, indent=2, width=20)
print(ast)