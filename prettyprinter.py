#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:16:28 2018

@author: huub
"""
import collections

_INil = collections.namedtuple('_INil', '')
_IStr = collections.namedtuple('_IStr', 'contents')
_IWord = collections.namedtuple('_IWord', 'contents')
_INewline = collections.namedtuple('_INewline', '')
_IAppend = collections.namedtuple('_IAppend', 'left right')

class INil(_INil):
  
  def flatten(self, worklist, context):
    flatten_tail(worklist, context)

class IStr(_IStr):
  
  def flatten(self, worklist, context):
    head = self.contents
    tail = flatten_tail(worklist, context.false())
    return head + tail

class IWord(_IWord):

  def flatten(self, worklist, context):
    head = self.contents
    tail = flatten_tail(worklist, context.true())
    if context.separator:
      s = ' '
    else:
      s = ''
    return s + head + tail
  
class INewline(_INewline):
    
  def flatten(self, worklist, context):
    tail = flatten_tail(worklist, context.false())
    margin = '\n{:>{width}}'.format('', width=context.indent)
    return margin + tail

class IAppend(_IAppend):
  
  def flatten(self, worklist, context):
    return self.left.flatten([self.right] + worklist, context)

class PrintContext():
  
  def __init__(self, separator, indent):
    self.separator = separator
    self.indent = indent
    
  def false(self):
    return PrintContext(False, self.indent)
  
  def true(self):
    return PrintContext(True, self.indent)

def flatten_tail(worklist, context):
  if len(worklist) > 0:
    return worklist[0].flatten(worklist[1:], context)
  return ''
  
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

def display(expr):
  context = PrintContext(False, 0)
  print_struct = expr.pp()
  return print_struct.flatten([], context)
