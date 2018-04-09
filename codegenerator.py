#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 12:24:32 2018

@author: huub
"""
import collections

class CodeGenerator:
    
    def c_number(self, ast):
        return ENum(int(ast))
    
    def c_variable(self, ast) :
        return EVar(ast)
    
    def c_let_expression(self, ast):
        return ELet(isRec=False, deflist=ast['deflist'], expr=ast['expr'])
    
    def c_letrec_expression(self, ast):
        return ELet(isRec=True, deflist=ast['deflist'], expr=ast['expr'])
    
    def c_case_expression(self, ast):
        return ECase(expr=ast['expr'], alts=ast['alts'])
    
    def c_alternative(self, ast):
        return EAlt(tag=ast['tag'], vars=ast['vars'], expr=ast['expr'])
    
    def c_lambda_expression(self, ast):
        return ELam(pars=ast['pars'], body=ast['body'])
    
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
        ap = EAp(fun=operator, arg=ast[0])
        i = 2
        while i < ast_len:
            arg = ast[i]
            ap = EAp(fun=ap, arg=arg)
            i = i+2
        return ap
    
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
        

EVar    = collections.namedtuple('EVar', 'ident')
ENum    = collections.namedtuple('ENum', 'intVal')
EConstr = collections.namedtuple('EConstr', 'tag arity')
EAp     = collections.namedtuple('EAp', 'fun arg')
ELet    = collections.namedtuple('ELet', 'isRec deflist expr')
ECase   = collections.namedtuple('ECase', 'expr alts')
ELam    = collections.namedtuple('ELam', 'pars body')
EAlt    = collections.namedtuple('EAlt', 'tag vars expr')