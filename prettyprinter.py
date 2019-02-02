#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:16:28 2018

@author: huub
"""
import collections

INil = collections.namedtuple('INil', '')
IStr = collections.namedtuple('IStr', 'contents')
IWord = collections.namedtuple('IWord', 'contents')
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

def flatten(iseq_list):
  if (len(iseq_list) == 0):
    return ''
  iseq = iseq_list[0]
  iseq_list_tail = iseq_list[1:]
  if isinstance(iseq, INil):
    return flatten(iseq_list_tail)
  elif isinstance(iseq, IStr):
    return iseq.contents + flatten(iseq_list_tail)
  elif isinstance(iseq, IWord):
    return iseq.contents + ' ' + flatten(iseq_list_tail)
  elif isinstance(iseq, IAppend):
    return flatten([iseq.left] + [iseq.right] + iseq_list_tail)
  else:
    print('Unknown type for iseq ' + iseq)
    return flatten(iseq_list_tail)


def display(expr):
  return flatten([expr.pp(False)])
