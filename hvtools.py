#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:39:29 2018

@author: huub

Handige tools van HvT voor het werken met tatsu grammatica's
"""
import tatsu

def read_file(name):
    with open(name, 'r') as input:
        contents = input.read()
    return contents

def write_file(name, contents):
    with open(name, 'w') as output:
        output.write(contents)

def generate_parser(basename):
    grammarname = basename + '.tatsu'
    filename = basename + '.parser.py'
    classname = basename[0].upper() + basename[1:]
    grammar = read_file(grammarname)
    p = tatsu.to_python_sourcecode(grammar, classname)
    write_file(filename, p)
