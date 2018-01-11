#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:03:14 2018

@author: vyk35227
"""

import turtle as t
t.width(2)
b = 5
t.speed(0)
y = 180

def kruh(a,b):
    for i in range(b):
        t.circle(120,360)
        t.left(30)
                
#kruh(0,12)

def nuhel(a,b,c):
    for i in range(c):
        for i in range(a):
            t.forward(20)
            t.left(72)
            for i in range(b):
                t.left(72)
                t.forward(23)
            
#nuhel(5,5,1)

def ctver(a,b):
    for i in range(a):
        t.forward(30)
        t.left(90)

s = 45
n = 4        
r = s/(2*(180/n))
ctver(4,0)
for i in range(1):
    y = y + 90
    t.setheading(y)
    t.circle(15,90)
    t.left(90)
    t.forward(r)

"""
t.forward(20)
t.right(180)
t.forward(20)


r = S/2sin(180/n)
"""