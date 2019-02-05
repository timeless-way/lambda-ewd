#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:16:28 2018

@author: huub
"""
import collections
import pprint

INil = collections.namedtuple('INil', '')
IStr = collections.namedtuple('IStr', 'contents')
IWord = collections.namedtuple('IWord', 'contents')
INewline = collections.namedtuple('INewline', '')
IAppend = collections.namedtuple('IAppend', 'left right')

def append(*contents):
  contents = list(filter(lambda c: not isinstance(c, INil), contents))
  if len(contents) == 0:
    return INil()
  elif len(contents) == 1:
    return contents[0]
  else:
    tree = IAppend(contents[0], contents[1])
    for c in contents[2:]:
      tree = IAppend(tree, c)
  return tree

def flatten(iseq_list, separator, indent):
  if (len(iseq_list) == 0):
    return ''
  iseq = iseq_list[0]
  iseq_list_tail = iseq_list[1:]
  if isinstance(iseq, INil):
    return flatten(iseq_list_tail, separator, indent)
  elif isinstance(iseq, IStr):
    return iseq.contents + flatten(iseq_list_tail, False, indent)
  elif isinstance(iseq, IWord):
    return flatten_word(iseq_list, separator, indent)
  elif isinstance(iseq, INewline):
    return flatten_newline(iseq_list, separator, indent)
  elif isinstance(iseq, IAppend):
    return flatten([iseq.left] + [iseq.right] + iseq_list_tail, separator, indent)
  else:
    print('Unknown type for iseq ' + iseq)
    return flatten(iseq_list_tail, separator, indent)

def flatten_word(iseq_list, separator, indent):
  iseq = iseq_list[0]
  iseq_list_tail = iseq_list[1:]
  s1 = flatten(iseq_list_tail, True, indent)
  if separator:
    s0 = ' '
  else:
    s0 = ''
  return s0 + iseq.contents + s1

def flatten_newline(iseq_list, separator, indent):
  iseq_list_tail = iseq_list[1:]
  margin = '\n{:>{width}}'.format('', width=indent)
  return margin + flatten(iseq_list_tail, False, indent)
  
def display(expr):
  print_struct = expr.pp()
  return flatten([print_struct], False, 0)
