#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:57:20 2018

@author: vyk35227
"""

from math import sin, cos, tan

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def root(a):
    return a ** (1/2)

functions = {"+": (2, plus), "-": (2, minus),
             "*": (2, lambda a,b: a * b),
             "/": (2, lambda a,b: a / b),
             "**": (2, lambda a,b: a ** b),
             "root": (1, root), "sin": (1, sin),
             "cos": (1, cos), "tg": (1, tan)          }

stack = []
while True:
    radek = input(str(stack) + " > ")
    radek = radek.split()
    for token in radek:
        if token == "kill" or token == "quit":
            exit(0)
        
        elif token in functions:
            if len(stack) >= functions[token][0]:
                a = stack.pop()
                b = stack.pop()
                stack.append(functions[token][1](a,b))
                
          
           
        else:
            try:
                stack.append(float(token))
            except:
                print( '"{}"' ' není ani funkce ani číslo'.format(token))
            
"""
elif sin or cos or tg in token:
    a = stack.pop()
    stack.append(functions[token][1](a)
41
"""           