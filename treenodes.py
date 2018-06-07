#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:33:57 2018

@author: huub
"""

import collections
import prettyprinter as pp

_EProg   = collections.namedtuple('EProg', 'supercombinators')
_ESc     = collections.namedtuple('ESc', 'lhs expr')
_ELhs    = collections.namedtuple('ELhs', 'name pars')
_EBind   = collections.namedtuple('EBind', 'name val')
_EVar    = collections.namedtuple('EVar', 'ident')
_ENum    = collections.namedtuple('ENum', 'intVal')
_EConstr = collections.namedtuple('EConstr', 'tag arity')
_EAp     = collections.namedtuple('EAp', 'fun arg')
_ELet    = collections.namedtuple('ELet', 'isRec deflist expr')
_ECase   = collections.namedtuple('ECase', 'expr alts')
_ELam    = collections.namedtuple('ELam', 'par body')
_EAlt    = collections.namedtuple('EAlt', 'tag vars expr')

class Prog(_EProg):
    
    def pp(self):
        return(pp.IStr('Prog'))

class Sc(_ESc):
    
    def pp(self):
        return pp.append(self.lhs.pp(), pp.IStr('='), self.expr.pp())

class Lhs(_ELhs):
    
    def pp(self):
        if len(self.pars) == 0:
            return pp.IStr(self.name)
        else:
            parlist = [pp.IStr(par) for par in self.pars]
            return pp.IAppend(pp.IStr(self.name), pp.append(*parlist))

class Bind(_EBind):
    
    def pp(self):
        return pp.IStr('Bind')

class Var(_EVar):
    
    def pp(self):
        return pp.IStr(self.ident)

class Num(_ENum):
    
    def pp(self):
        return pp.IStr(str(self.intVal))

class Constr(_EConstr):
    
    def pp(self):
        return pp.IStr('Constr')

class Ap(_EAp):
    
    def pp(self):
        return pp.IAppend(self.fun.pp(), self.arg.pp())

class Let(_ELet):
    
    def pp(self):
        return pp.IStr('Let')

class Case(_ECase):
    
    def pp(self):
        return pp.IStr('Case')

class Lam(_ELam):
    
    def pp(self):
        return pp.IStr('Lam')

class Alt(_EAlt):
    
    def pp(self):
        return pp.IStr('Alt')

