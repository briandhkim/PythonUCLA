# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:42:23 2017

@author: Brian


Create a MathVector class to represent N-dimensional mathematical vectors


Initializer:
    - if there is a single numerical argument(assumed to be an integer), 
    the MathVector should represent a zero vector(vector of all zero components)
    of the specified number of dimensions
    - if there is a single list or tuple argument or if  there are multiple arguments,
    the MathVector should represent a vector with the specified components
    - the constructor does not need to work properly for any other input cases
    
Methods:
    - get_el    : returns the i-th component of the vector(1-indexed)
    - neg       : returns the negative of the original vector(leaving original unchanged)
    - mag       : returns the magnitude of the vector
    - dot       : returns the dot product of the vector and another vector
    - plus      : returns the sum of the vector and another vector
    - sp        : returns the product of the vector and a scalar
    - print_me  : prints a representation of the vector to the console
    
Magic methods for built in operators and functions [],-(negation), abs(for magnitude),
    *, +, and print call the appropriate methods mentioned above. * operator should
    work for both dot and sp(before or after MathVector)
    
"""



import math

class MathVector:
    def __init__(self, *args):
        if type(args[0]) == int and len(args) == 1:
            self.elementContent = [0 for x in range(args[0])]    
            self.elementCount = len(self.elementContent)  
        elif len(args) == 1:
            self.elementCount= len(args[0])
            self.elementContent = [args[0][x] for x in range(self.elementCount)]
        #elif len(args)==1:
        #    self.elementContent = [0 for x in range(args[0])]    
        #    self.elementCount = len(self.elementContent)  
        else:
            self.elementContent = [x for x in args]
            self.elementCount = len(args)
            
    def __getitem__(self, index):
        return self.elementContent[index-1]    
        
    def __str__(self):
        return str(self.elementContent)
        
        
    def get_el(self, index):
        return self.elementContent[index-1]        
    
    def neg(self):
        neg_list = [-1*x for x in self.elementContent]
        return_list = MathVector(neg_list)
        return return_list
        
    def __neg__(self):
        #neg_list = [-1*x for x in self.elementContent]
        #return_list = MathVector(neg_list)
        return_list = MathVector(self.elementContent)      
        return return_list.neg()
    
    def mag(self):
        magnitude = math.sqrt(sum(i*i for i in self.elementContent))
        return magnitude
        
    def dot(self, other):
        dot_prod = sum(self.elementContent[x]*other.elementContent[x] for x in range(self.elementCount))
        return dot_prod
    
    def plus(self, other):
        p = MathVector([self.elementContent[x] + other.elementContent[x] for x in range(self.elementCount)])
        return p
        
    def __add__(self, other):
        #x = MathVector([self.elementContent[x] + other.elementContent[x] for x in range(self.elementCount)])
        x = self.plus(other)      
        return x
        
    def sp(self, num):
        s = MathVector([self.elementContent[x] * num for x in range(self.elementCount)])
        return s
    
    def __abs__(self):
       return self.mag()
    
    def __mul__(self, other):
        if type(other) == int:
            return self.__rmul__(other)
        else:
            x =self.dot(other)
            return x
        
    def __rmul__(self,other):
        return self.sp(other)
        
    
    def print_me(self):
        print self.elementContent
        #print self.elementCount
        
        
        
u = MathVector(5)
print "u =",
u.print_me()

v = MathVector([2,3,6])
print "v =",
v.print_me()

w = MathVector(1,2,3)
print "w =",
w.print_me()

print v.get_el(2)
v.neg().print_me()
print v.mag()
print v.dot(w)
v.plus(w).print_me()
v.sp(3).print_me()

print v
print v[2]
print -v
print abs(v)
print v*w
print v+w
print v*3
print 3*v
