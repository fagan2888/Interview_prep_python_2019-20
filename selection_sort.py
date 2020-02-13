#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:17:28 2020

@author: liwenhuang

selection sort
find the min at each iteration, place it at the begining of the array
"""

nums = [4, 8, 0, 2, 4, 1, 3]

min_idx = 0
n = len(nums)
while min_idx < n -1:
    for i in range(min_idx, n):
        if nums[i] < nums[min_idx]:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    
    min_idx += 1
        
        
        
