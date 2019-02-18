#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:33:57 2018

@author: huub
"""

import collections
import prettyprinter as ppr

from abc import ABC, abstractmethod

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

class TreeNode(ABC):
  
  @abstractmethod
  def pp(self, packed=False):
    return ppr.IWord('No method pp defined for ' + str(type(self)))

class Prog(TreeNode, EProg):
    
  def pp(self, packed=False):
    combinator_list = []
    for combinator in self.supercombinators:
      combinator_list = combinator_list + [combinator.pp()]
    seq1 = ppr.ISequence(combinator_list)
    nl = ppr.IStr(';\n')
    seq2 = seq1.join(nl)
    return seq2

class Sc(TreeNode, ESc):
    
  def pp(self, packed=False):
    return ppr.sequence(self.lhs.pp(), ppr.IWord('='), self.expr.pp())

class Lhs(TreeNode, ELhs):
    
  def pp(self, packed=False):
    if len(self.pars) == 0:
      return ppr.IWord(self.name)
    else:
      parlist = [ppr.IWord(par) for par in self.pars]
      return ppr.sequence(ppr.IWord(self.name), ppr.ISequence(parlist))

class Bind(TreeNode, EBind):
    
  def pp(self, packed=False):
    _name = self.name.pp(packed)
    _eq = ppr.IWord('=')
    _val = self.val.pp(packed)
    return ppr.sequence(_name, _eq, _val)
   
class Var(TreeNode, EVar):
    
  def pp(self, packed=False):
    return ppr.IWord(self.ident)

class Num(TreeNode, ENum):
    
  def pp(self, packed=False):
    return ppr.IWord(str(self.intVal))

class Constr(TreeNode, EConstr):
    
  def pp(self, packed=False):
    _tag = self.tag.pp(packed)
    _arity = self.arity.pp(packed)
    _pack = ppr.IStr(' Pack')
    _lbrace = ppr.IStr('{')
    _rbrace = ppr.IStr('}')
    _comma = ppr.IStr(', ')
    return ppr.sequence(_pack, _lbrace, _tag, _comma, _arity, _rbrace)

class Ap(TreeNode, EAp):
    
  def pp(self, packed=False):
    pre = ppr.IStr('(') if packed else ppr.INil()
    post = ppr.IStr(')') if packed else ppr.INil()
    return ppr.sequence(pre, self.fun.pp(False), self.arg.pp(True), post)

class Let(TreeNode, ELet):
    
  def pp(self, packed=False):
    _ob = ppr.IOpenBlock()
    _cb = ppr.ICloseBlock()
    _nl = ppr.INewline()
    
    _let = ppr.IWord('letrec') if self.isRec else ppr.IWord('let')
    _in = ppr.IWord('in')
    
    _definitions = self.pp_definitions(self.deflist, packed)
    pp_expr = self.expr.pp(packed)
    return ppr.sequence(_ob, _let, _ob, _definitions, _cb, _in, pp_expr, _cb)
  
  def pp_definitions(self, definitions, packed):
    _nl = ppr.sequence(ppr.IStr(';'), ppr.INewline())
    defs = ppr.ISequence([definition.pp(packed) for definition in definitions])
    return defs.join(_nl)

class Case(TreeNode, ECase):
    
  def pp(self, packed=False):
    _ob = ppr.IOpenBlock()
    _cb = ppr.ICloseBlock()
    
    _case = ppr.IWord('case')
    _of = ppr.IWord('of')
    _esac = ppr.IWord('esac')
    
    pp_expr = self.expr.pp(packed)
    alternatives = self.pp_alts(self.alts, packed)
    pp_alts = ppr.sequence(_ob, alternatives, _cb)
    return ppr.sequence(_ob, _case, pp_expr, _of, pp_alts, _esac, _cb)
  
  def pp_alts(self, alternatives, packed):
    alts = ppr.ISequence([alt.pp(packed) for alt in alternatives])
    nl = ppr.sequence(ppr.IStr(';'), ppr.INewline())
    return alts.join(nl)
  
class Lam(TreeNode, ELam):
    
  def pp(self, packed=False):
    _lambda = ppr.IStr('\\')
    _dot = ppr.IStr('.')
    _par = self.par.pp(packed)
    _body = self.body.pp(packed)
    return ppr.sequence(_lambda, _par, _dot, _body)

class Alt(TreeNode, EAlt):
    
  def pp(self, packed=False):
    tag = ppr.sequence(ppr.IStr('<'), self.tag.pp(packed), ppr.IStr('> '))
    varlist = [var.pp(packed) for var in self.vars]
    expr = self.expr.pp(packed)
    return ppr.sequence(tag, ppr.ISequence(varlist), ppr.IWord('->'), expr)

