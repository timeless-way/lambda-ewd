#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 12:24:32 2018

@author: huub
"""
import collections

class CodeGenerator:
    
    def c_program(self, ast):
        return self.remove_interpunction(ast, [";"])
    
    def c_super_combinator(self, ast):
        return ESc(lhs=ast['lhs'], expr=ast['expr'])
    
    def c_lhs(self, ast):
        return ELhs(name=ast['name'], pars=ast['pars'])
    
    def c_number(self, ast):
        return ENum(int(ast))
    
    def c_variable(self, ast) :
        return EVar(ast)
    
    def c_let_expression(self, ast):
        return ELet(isRec=False, deflist=ast['deflist'], expr=ast['expr'])
    
    def c_letrec_expression(self, ast):
        return ELet(isRec=True, deflist=ast['deflist'], expr=ast['expr'])

    def c_definition_list(self, ast):
        return self.remove_interpunction(ast, [";"])
    
    def c_definition(self, ast):
        return EBind(name=ast['name'], val=ast['val'])
    
    def c_case_expression(self, ast):
        return ECase(expr=ast['expr'], alts=ast['alts'])
    
    def c_alternative(self, ast):
        return EAlt(tag=ast['tag'], vars=ast['vars'], expr=ast['expr'])
    
    def c_lambda_expression(self, ast):
        return self.create_lambda_abstraction(ast['pars'], ast['body'])
    
    def c_constructor(self, ast):
        return EConstr(tag=ast['tag'], arity=ast['arity'])
    
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
        operator = EVar(ast[1])
        ap1 = EAp(fun=operator, arg=ast[0])
        ap2 = EAp(fun=ap1, arg=ast[2])
        i = 4
        while i < ast_len:
            ap1 = EAp(fun=operator, arg=ap2)
            ap2 = EAp(fun=ap1, arg=ast[i])
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
        ap = EAp(fun=ast[0], arg=ast[1])
        i = 2
        while i < ast_len:
            arg = ast[i]
            ap = EAp(fun=ap, arg=arg)
            i = i+1
        return ap
    
    def create_lambda_abstraction(self, pars, body):
        if len(pars) == 1:
            return ELam(par=pars[0], body=body)
        else:
            abstr = self.create_lambda_abstraction(pars[1:], body)
            return ELam(par=pars[0], body=abstr)
    
    def remove_interpunction(self, sequence, interpunctions):
        return [item for item in sequence if item not in interpunctions]
        
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

# The next section contains some utilities to manipulate the parse tree

def is_atomic(expr):
    return (isinstance(expr, EVar) or isinstance(expr, ENum))

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
