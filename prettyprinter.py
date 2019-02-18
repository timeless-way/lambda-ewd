#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:16:28 2018

@author: huub
"""
import collections
from abc import ABC, abstractmethod

_INil = collections.namedtuple('_INil', '')
_IStr = collections.namedtuple('_IStr', 'string')
_ISequence = collections.namedtuple('_Sequence', 'contents')

class _ISeq(ABC):
  
  @abstractmethod
  def flatten(self, worklist, context):
    return 'No flatten defined for ' + str(type(self))

class INil(_ISeq, _INil):
  
  def flatten(self, worklist, context):
    flatten_tail(worklist, context)

class IStr(_ISeq, _IStr):
  
  def flatten(self, worklist, context):
    head = self.string
    tail = flatten_tail(worklist, context.false())
    return head + tail

class IWord(_ISeq, _IStr):

  def flatten(self, worklist, context):
    head = self.string
    tail = flatten_tail(worklist, context.true())
    if context.separator:
      s = ' '
    else:
      s = ''
    return s + head + tail
  
class INewline(_ISeq, _INil):
    
  def flatten(self, worklist, context):
    tail = flatten_tail(worklist, context.false())
    margin = '\n{:>{width}}'.format('', width=context.indent)
    return margin + tail

class ISequence(_ISeq, _ISequence):
  
  def flatten(self, worklist, context):
    head = self.contents[0]
    tail = self.contents[1:] 
    return head.flatten(tail + worklist, context)
  
  def join(self, sep):
    contents = self.contents
    new_contents = []
    for iseq in contents[:-1]:
      new_contents = new_contents + [iseq, sep]
    new_contents = new_contents + [contents[-1]]
    return ISequence(new_contents)

class IOpenBlock(_ISeq, _INil):
  
  def flatten(self, worklist, context):
    newcontext = context.false().increment()
    tail = flatten_tail(worklist, newcontext)
    margin = '\n{:>{width}}'.format('', width=newcontext.indent)
    return margin + tail

class ICloseBlock(_ISeq, _INil):
  
  def flatten(self, worklist, context):
    newcontext = context.false().decrement()
    tail = flatten_tail(worklist, newcontext)
    margin = '\n{:>{width}}'.format('', width=newcontext.indent)
    return margin + tail

class PrintContext():
  
  def __init__(self, separator, indent):
    self.separator = separator
    self.indent = indent
    self.block_increment = 2
  
  def true(self):
    return PrintContext(True, self.indent)

  def false(self):
    return PrintContext(False, self.indent)
  
  def increment(self):
    return PrintContext(self.separator, self.indent + self.block_increment)
  
  def decrement(self):
    return PrintContext(self.separator, self.indent - self.block_increment)
  
def flatten_tail(worklist, context):
  if len(worklist) > 0:
    return worklist[0].flatten(worklist[1:], context)
  return ''
  
def sequence(*contents):
  _contents = list(filter(lambda c: not isinstance(c, INil), contents))
  return ISequence(_contents)

def display(expr):
  context = PrintContext(False, 0)
  print_struct = expr.pp()                                           
  #print(print_struct)
  return print_struct.flatten([], context)
