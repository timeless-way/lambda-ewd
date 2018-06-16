#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:16:28 2018

@author: huub
"""
import collections

def pretty(expr):
    return expr.pp()

INil = collections.namedtuple('INil', '')
IStr = collections.namedtuple('IStr', 'contents')
IAppend = collections.namedtuple('IAppend', 'left right')

def append(*contents):
    if len(contents) == 0:
        return INil()
    elif len(contents) == 1:
        return contents[0]
    else:
        tree = IAppend(contents[0], contents[1])
        for c in contents[2:]:
            tree = IAppend(tree, c)
        return tree

def flatten(iseq):
    if isinstance(iseq, INil):
        return ''
    elif isinstance(iseq, IStr):
        return iseq.contents
    elif isinstance(iseq, IAppend):
        right_string = flatten(iseq.right)
        left_string = flatten(iseq.left)
        return left_string + ' ' + right_string
    else:
        return 'flatten: ???' + str(iseq)

def display(expr):
    return flatten(pretty(expr))
