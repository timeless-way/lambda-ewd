#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:35:10 2019

@author: huub
"""

from prettyprinter import IStr, IWord, IAppend, PrintContext, append

ctx = PrintContext(False, 0)

s1 = IStr('s1')
s2 = IStr('s2')

w1 = IWord('w1')
w2 = IWord('w2')

a1 = IAppend(s1, s2)
a2 = IAppend(w1, w2)

a3 = append(s1, w1, w2, s2)

def flt(iseq):
  return iseq.flatten([], ctx)