#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:39:29 2018

@author: huub
"""

def read_file(name):
    with open(name, 'r') as input:
        contents = input.read()
    return contents

