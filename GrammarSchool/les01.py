#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 08:26:36 2018

@author: huub
"""

import pprint
import json
from tatsu import parse
from tatsu.util import asjson

def main():
    with open('grammar1.tatsu', 'r') as input:
        GRAMMAR=input.read().replace('\n', ' ')
    ast = parse(GRAMMAR, '3 + 5 * ( 10 - 20 )')
    print('PPRINT')
    pprint.pprint(ast, indent=2, width=20)
    print()

    print('JSON')
    print(json.dumps(asjson(ast), indent=2))
    print()