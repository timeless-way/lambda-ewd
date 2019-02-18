#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:35:10 2019

@author: huub
"""

from prettyprinter import IStr, IWord, IAppend, INewline, IOpenBlock, ICloseBlock, PrintContext, append, sequence

ctx = PrintContext(False, 0)

s1 = IStr('s1')
s2 = IStr('s2')

w1 = IWord('w1')
w2 = IWord('w2')

a1 = IAppend(s1, s2)
a2 = IAppend(w1, w2)

a3 = append(s1, w1, w2, s2)

nl = INewline()
ob = IOpenBlock()
cb = ICloseBlock()

seq1 = sequence(w1, s1, s2, w2)
seq2 = sequence(w1, w2, w1, w2)
seq3 = sequence(w1, s1, w2, s2)
seq4 = sequence(s1, w1, w2, s2)
seq5 = sequence(s1, nl, s2, ob, s1, nl, s2, ob, s1, nl, s2, cb, s1, cb, s2)
seq6 = sequence(w1, nl, w2, ob, w1, nl, w2, ob, w1, nl, w2, cb, w1, cb, w2)

def flt(iseq):
  return iseq.flatten([], ctx)

print(flt(seq6))
