#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 12:24:32 2018

@author: huub
"""

import treenodes as tn
class CodeGenerator:
  
  def c_program(self, ast):
    return tn.Prog(self.remove_interpunction(ast, [";"]))

  def c_super_combinator(self, ast):
    return tn.Sc(lhs=ast['lhs'], expr=ast['expr'])

  def c_lhs(self, ast):
    return tn.Lhs(name=ast['name'], pars=ast['pars'])

  def c_number(self, ast):
    return tn.Num(int(ast))

  def c_variable(self, ast) :
    return tn.Var(ast)

  def c_let_expression(self, ast):
    return tn.Let(isRec=False, deflist=ast['deflist'], expr=ast['expr'])

  def c_letrec_expression(self, ast):
    return tn.Let(isRec=True, deflist=ast['deflist'], expr=ast['expr'])

  def c_definition_list(self, ast):
    return self.remove_interpunction(ast, [";"])

  def c_definition(self, ast):
    return tn.Bind(name=ast['name'], val=ast['val'])

  def c_case_expression(self, ast):
    return tn.Case(expr=ast['expr'], alts=ast['alts'])

  def c_alternative(self, ast):
    return tn.Alt(tag=ast['tag'], vars=ast['vars'], expr=ast['expr'])

  def c_lambda_expression(self, ast):
    return self.create_lambda_abstraction(ast['pars'], ast['body'])

  def c_constructor(self, ast):
    return tn.Constr(tag=ast['tag'], arity=ast['arity'])

  def c_parentheses(self, ast):
    return ast['expr']

  def c_expr1(self, ast):
    return self.create_operator_application(ast)

  def c_expr2(self, ast):
    return self.create_operator_application(ast)

  def c_expr3(self, ast):
    return self.create_operator_application(ast)

  def c_expr4(self, ast):
    return self.create_operator_application(ast)

  def c_expr5(self, ast):
    return self.create_operator_application(ast)

  def c_expr6(self, ast):
    return self.create_operator_application(ast)

  def c_expr7(self, ast):
    return self.create_operator_application(ast)

  def c_expr8(self, ast):
    return self.create_function_application(ast)

  def _default(self, ast):
    return ast

  def create_operator_application(self, ast):
    if not isinstance(ast, list):
      return ast
    ast_len = len(ast)
    if ast_len == 0:
      return None
    if ast_len == 1:
      return ast[0]
    operator = tn.Var(ast[1])
    ap1 = tn.Ap(fun=operator, arg=ast[0])
    ap2 = tn.Ap(fun=ap1, arg=ast[2])
    i = 4
    while i < ast_len:
      ap1 = tn.Ap(fun=operator, arg=ap2)
      ap2 = tn.Ap(fun=ap1, arg=ast[i])
      i = i+2
    return ap2

  def create_function_application(self, ast):
    if not isinstance(ast, list):
      return ast
    ast_len = len(ast)
    if ast_len == 0:
      return None
    if ast_len == 1:
      return ast[0]
    ap = tn.Ap(fun=ast[0], arg=ast[1])
    i = 2
    while i < ast_len:
      arg = ast[i]
      ap = tn.Ap(fun=ap, arg=arg)
      i = i+1
    return ap

  def create_lambda_abstraction(self, pars, body):
    if len(pars) == 1:
      return tn.Lam(par=pars[0], body=body)
    else:
      abstr = self.create_lambda_abstraction(pars[1:], body)
      return tn.Lam(par=pars[0], body=abstr)
    
  def remove_interpunction(self, sequence, interpunctions):
    return [item for item in sequence if item not in interpunctions]


# The next section contains some utilities to manipulate the parse tree

def is_atomic(expr):
  return (isinstance(expr, tn.Var) or isinstance(expr, tn.Num))

def left_hand_sides(program):
  return [sc.lhs for sc in program.ast]

def expressions(program):
  return [sc.expr for sc in program.ast]

def names(program):
  return [lhs.name for lhs in left_hand_sides(program)]

def parameters(program):
  return [lhs.pars for lhs in left_hand_sides(program)]

def binders_of(deflist):
  return [dfn.name for dfn in deflist]

def values_of(deflist):
  return [dfn.val for dfn in deflist]
