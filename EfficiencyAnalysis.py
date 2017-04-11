# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:26:41 2017

@author: Brian

This is simple analysis determining relative efficency of 
map, list comprehension, and for loops while perfoming identical
task with each strategy 
"""

import time

#case 1, for loop time
def f(x): return x**2
x = range(100000)
y = []

begin = time.clock()
for i in x:
    y.append(f(i))
end = time.clock()

print "case1: ", end-begin



#case2, write a lambda function g
g = lambda x: x**2
x = range (100000)
y = []

begin = time.clock()
for i in x:
    y.append(g(i))
end = time.clock()

print "case2: ", end-begin



#case 3, **2 operation in the loop 
x = range (100000)
y = []

begin = time.clock()
for i in x:
    y.append(i**2)
end = time.clock()

print "case3: ", end-begin



#case 4, initialize y to range(N)
y = range(100000)
x = []

begin = time.clock()
for i in range(len(y)):
    x.append(y[i]**2)
end= time.clock()

print "case4: ", end-begin



#case 5, use list comprehension
begin = time.clock()
y = [test5**2 for test5 in range(100000)]
end = time.clock()

print "case5: ", end-begin



#case 6, use map
def f(x): return x**2

begin = time.clock()
map(f, range(100000))
end = time.clock()

print "case6: ", end-begin

