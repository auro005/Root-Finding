# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 00:03:02 2021

@author: auro005
"""
from math import *

def f(x):
    return(x**3-3*x+1)

x_1 = -1000
x_2 = 100
n_steps = 0
while(abs(f(x_2))>10**-8):
    temp = x_2-f(x_2)*(x_2-x_1)/(f(x_2)-f(x_1))
    x_1 = x_2 
    x_2 = temp
    n_steps = n_steps+1

print(x_2,n_steps)