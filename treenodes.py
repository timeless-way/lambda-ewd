#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:33:57 2018

@author: huub
"""

import collections
import prettyprinter as ppr

EProg   = collections.namedtuple('EProg', 'supercombinators')
ESc     = collections.namedtuple('ESc', 'lhs expr')
ELhs    = collections.namedtuple('ELhs', 'name pars')
EBind   = collections.namedtuple('EBind', 'name val')
EVar    = collections.namedtuple('EVar', 'ident')
ENum    = collections.namedtuple('ENum', 'intVal')
EConstr = collections.namedtuple('EConstr', 'tag arity')
EAp     = collections.namedtuple('EAp', 'fun arg')
ELet    = collections.namedtuple('ELet', 'isRec deflist expr')
ECase   = collections.namedtuple('ECase', 'expr alts')
ELam    = collections.namedtuple('ELam', 'par body')
EAlt    = collections.namedtuple('EAlt', 'tag vars expr')

class Prog(EProg):
    
  def pp(self, packed=False):
    sc = self.supercombinators
    ppsc = ([ppr.IAppend(c.pp(), ppr.IStr(';\n')) for c in sc])
    return ppr.append(*ppsc)

class Sc(ESc):
    
  def pp(self, packed=False):
    return ppr.append(self.lhs.pp(), ppr.IWord('='), self.expr.pp())

class Lhs(ELhs):
    
  def pp(self, packed=False):
    if len(self.pars) == 0:
      return ppr.IWord(self.name)
    else:
      parlist = [ppr.IWord(par) for par in self.pars]
      return ppr.IAppend(ppr.IWord(self.name), ppr.append(*parlist))

class Bind(EBind):
    
  def pp(self, packed=False):
    return ppr.IStr('Bind')
   
class Var(EVar):
    
  def pp(self, packed=False):
    return ppr.IWord(self.ident)

class Num(ENum):
    
  def pp(self, packed=False):
    return ppr.IWord(str(self.intVal))

class Constr(EConstr):
    
  def pp(self, packed=False):
    return ppr.IStr('Constr')

class Ap(EAp):
    
  def pp(self, packed=False):
    pre = ppr.IStr('(') if packed else ppr.INil()
    post = ppr.IStr(')') if packed else ppr.INil()
    return ppr.append(pre, self.fun.pp(False), self.arg.pp(True), post)

class Let(ELet):
    
  def pp(self, packed=False):
    return ppr.IStr('Let')

class Case(ECase):
    
  def pp(self, packed=False):
    return ppr.IStr('Case')

class Lam(ELam):
    
  def pp(self, packed=False):
    return ppr.IStr('Lam')

class Alt(EAlt):
    
  def pp(self, packed=False):
    return ppr.IStr('Alt')

