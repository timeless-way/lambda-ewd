#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:39:29 2018

@author: huub

Handige tools van HvT voor het werken met tatsu grammatica's
"""
import tatsu

def read_file(name):
  with open(name, 'r') as input_file:
    contents = input_file.read()
  return contents

def write_file(name, contents):
  with open(name, 'w') as output:
    output.write(contents)

def generate_python_module(basename):
  grammarname = basename + '.tatsu'
  filename = basename + '_parser.py'
  classname = basename[0].upper() + basename[1:]
  grammar = read_file(grammarname)
  parser_text = tatsu.to_python_sourcecode(grammar, classname)
  write_file(filename, parser_text)

def generate_parser_instance(basename):
  grammarname = basename + '.tatsu'
  classname = basename[0].upper() + basename[1:]
  grammar = read_file(grammarname)
  parser = tatsu.compile(grammar, name=classname)
  return parser
