#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 00:37:44 2018

@author: huub
"""

import hvtools as ht
import pprint
import codegenerator as cg
import prettyprinter as ppr
import ewd_parser

'''A Language instance has a grammar and a semantics.'''
class Language:

  '''
  Either grammar_file or parser_instance must be specified, but not both!
  '''
  def __init__(self, grammar_file=None, parser_instance=None, semantics=None):
    if grammar_file and parser_instance:
      self.parser = None
      print('Error: both grammar_file and parser_instance specified.')
    elif grammar_file:
      self.parser = ht.generate_parser_instance(grammar_file)
    elif parser_instance:
      self.parser = parser_instance
    else:
      self.parser = None
      print('Error: No grammar_file or parser_instance specified.')
    self.semantics = semantics

  def parse(self, text, **kwargs):
    return self.parser.parse(text, semantics=self.semantics, **kwargs)

  '''
  A Program has a source and a Language in which the source is written and that
  contains the interpretational semantics of the program.
  '''
class Program:

  def __init__(self, source_file, language):
    self.source = ht.read_file(source_file)
    self.language = language
    self.ast = self.language.parse(self.source)

  def show_ast(self):
    pprint.pprint(self.ast, indent=2, width=20)

  def show_source(self):
    print(self.source)

# Usage examples:

parser = ewd_parser.EwdParser()
#ewd = Language(parser_instance=parser)

print('Creating language:... ', end='')
#ewd = Language(grammar_file='ewd', semantics=cg.CodeGenerator())
ewd = Language(parser_instance=parser, semantics=cg.CodeGenerator())
print('OK')
print('Creating program... ', end='')
test = Program('ewd-source/standard-prelude.ewd', ewd)
#test = Program('ewd-source/test.ewd', ewd)

print('OK')
#print('Source:')
#test.show_source()
print('AST:')
test.show_ast()
print('\n==============================================\n')
print(ppr.display(test.ast))