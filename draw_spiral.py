#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:46:24 2020

@author: liwenhuang
found this link
https://www.101computing.net/python-turtle-my-house/
"""

from turtle import * 

setup(500, 500)
t1 = Turtle()
t1.hideturtle()
t1.speed(10)

for i in range(500):
    t1.forward(2*i)
    t1.right(120)

