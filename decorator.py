#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:17:36 2020

@author: liwenhuang
notes on decorator
"""

# function is a first class object
def uppercase_decorator(function):
    def wrapper():
        func = function() # note that this function object has been called
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi) # this is a function object
decorate() # now the function object is called

# to do the above with decorator, this produce the same output
@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()
#Out[208]: 'HELLO THERE'

# multiple decorator can be applied at the same time
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()

#Out[209]: ['HELLO', 'THERE']