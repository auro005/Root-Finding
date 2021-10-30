# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 22:32:22 2021

@author: auro005
"""

from math import *

def f(x):
    return(x**3-3*x+1)

def f_1(x):
    return(3*x**2-3)

x = -2.0 #initial guess

diff = 1.0
n_steps = 0
while(abs(diff)>10**-8):
    t = x
    x = x-(f(x)/f_1(x))
    diff = t-x
    n_steps = n_steps+1
    
print(x,n_steps)
    

