#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 00:37:44 2018

@author: huub
"""

import hvtools

"""A Language instance has a grammar and a semantics."""
class Language:
    
    def __init__(self, grammar_file):
        self.grammar = hvtools.generate_parser_instance(grammar_file)
    
    def parse(self, text):
        return self.grammar.parse(text)

"""
A Program has a source and a Language in which the source is written and that
contains the interpretational semantics of the program.
"""

class Program:
    
    def __init__(self, source_file, language):
        self.source = hvtools.read_file(source_file)
        self.language = language
    
    def compile(self):
        self._ast = self.language.parse(self.source)
    
    