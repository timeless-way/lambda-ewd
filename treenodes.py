#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:33:57 2018

@author: huub
"""

import collections
import prettyprinter as pretty

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
    
    def pp(self, packed=False):
        return(pretty.IStr('Prog'))

class Sc(_ESc):
    
    def pp(self, packed=False):
        return pretty.append(self.lhs.pp(packed), pretty.IStr('='), self.expr.pp(packed))

class Lhs(_ELhs):
    
    def pp(self, packed=False):
        if len(self.pars) == 0:
            return pretty.IStr(self.name)
        else:
            parlist = [pretty.IStr(par) for par in self.pars]
            return pretty.IAppend(pretty.IStr(self.name), pretty.append(*parlist))

class Bind(_EBind):
    
    def pp(self, packed=False):
        return pretty.IStr('Bind')

class Var(_EVar):
    
    def pp(self, packed=False):
        return pretty.IStr(self.ident)

class Num(_ENum):
    
    def pp(self, packed=False):
        return pretty.IStr(str(self.intVal))

class Constr(_EConstr):
    
    def pp(self, packed=False):
        return pretty.IStr('Constr')

class Ap(_EAp):
    
    def pp(self, packed=False):
        pre = pretty.IStr('(') if packed else pretty.INil()
        post = pretty.IStr(')') if packed else pretty.INil()
        return pretty.append(pre, self.fun.pp(False), self.arg.pp(True), post)

class Let(_ELet):
    
    def pp(self, packed=False):
        return pretty.IStr('Let')

class Case(_ECase):
    
    def pp(self, packed=False):
        return pretty.IStr('Case')

class Lam(_ELam):
    
    def pp(self, pre='', post=''):
        return pretty.IStr('Lam')

class Alt(_EAlt):
    
    def pp(self, pre='', post=''):
        return pretty.IStr('Alt')

