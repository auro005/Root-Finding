# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:18:37 2021

@author: auro005
"""
#BISECTION METHOD
from math import *
def f(x):
    return (x**3-3*x+1)


a = 0.0
b = 1.0
diff = b-a
x_m = (b+a)/2.0
nsteps = 0
while(abs(diff)>10**(-12) and abs(x_m)>10**(-12)):
    
    if(f(a)*f(x_m)<=0.0):
        b = x_m
    else:
        a = x_m
    x_m = (b+a)/2.0
    diff = b-a
    nsteps = nsteps+1
print(x_m,nsteps)        
