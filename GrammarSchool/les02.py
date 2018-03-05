#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:54:19 2018

@author: huub
Create a parser object so several expressions can be parsed by the same parser.
"""

import tatsu
from hvtools import read_file, generate_python_module

GRAMMAR = read_file('grammar1.tatsu')
EXPRESSION_1 = '1 + 2 + 3 + 4'
EXPRESSION_2 = '1*(3+4)'

# generate a parseer dynamically:
parser = tatsu.compile(GRAMMAR)

# generate a python module that contains the parser.
# this module must be imported before it can be used.
generate_python_module('grammar1')