#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:16:59 2020

@author: liwenhuang
quick select kth smallest element in an array
"""
import random

def select(values, k):
    pivot = random.choice(values)
    low, high = [], []
    for value in values:
        if value < pivot:
            low.append(value)
        elif value > pivot:
            high.append(value)
    if k < len(low):
        return select(low, k)
    k += len(high) - len(values)
    if k < 0:
        return pivot
    return select(high, k)

values = [1, 2, 3, 4, 5, 6, 7]
select(values, 2)