#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:32:59 2020

@author: liwenhuang

backpack problem 
"""

max_size = 10
max_time = 10
sizes = [2, 3, 5, 7]
times = [2, 7, 1, 5]
values = [1, 5, 2, 4]


'''
very brute force solution with O(2^n) time, this is what I should probably at least implement today
this solution will surely time out when input gets big, also occupies extra space to store all the combination 
although this is a very stupid solution, it is easier to retrive the combination later
'''

# how to get the subset of length of n?
def find_subsets(n):
    if n == 0:
        return None
    if n == 1:
        return [[0], [1]]
    
    last_step = find_subsets(n-1)
    result = []
    for subset in last_step:
        result.append(subset + [0])
        result.append(subset + [1])
    
    return result

def max_val_pack(max_size, max_time, sizes, times, values):
    n = len(sizes)
    ways = find_subsets(n)
    
    # check when the size does not overflow, what is the max_value
    max_value = 0
    for way in ways:
        load_size = sum([sizes[i] for i in range(n) if way[i]])
        load_time = sum([times[i] for i in range(n) if way[i]])
        if load_size <= max_size and load_time <= max_time: # satisfy the contraints
            load_value = sum([values[i] for i in range(n) if way[i]])
            if load_value > max_value:
                max_value = load_value
                best_way = way
    
    print('The best way to pack the truck is:', best_way, 'the maximal value is:', max_value)
    return (best_way, max_value)

#max_val_pack(max_size, max_time, sizes, times, values)
#The best way to pack the truck is: [1, 1, 1, 0] the maximal value is: 8
#Out[74]: ([1, 1, 1, 0], 8)

'''
The right way to solve this problem would be to use dynamic programming, o(n^2) time, space O(max_size*n)

initiate a 2d array dp for computting, cell dp[i][j] represent best value status at item i when the size is j
dp[0][...] = 0, dp[...][0] = 0, therefore, at each row i, the problem simplies to when size is j, what is the maximal value if we pack i or not
pack item i, dp[i - 1][j - sizes[i]] + values[i] (j-sizes[i]>0) or we do not pack i, dp[i - 1][j]
at last, return the cell value at the bottom left corner

this solution can be optimized to O(max_size) space when using a rolling array, keep only the dp[i][...] as we move forward
'''
max_size = 10
max_time = 10
sizes = [2, 3, 5, 7]
times = [2, 7, 1, 5]
values = [1, 5, 2, 4]

def dp_best_value(max_size, max_time, sizes, times, values):
    # fullfil the size requirement  
    dp_size = [0 for i in range(max_size+1)]
    n = len(sizes)
    for i in range(n):
        for j in range(max_size, sizes[i]-1, -1):
            dp_size[j] = max(dp_size[j], dp_size[j-sizes[i]] + values[i])
    
    # fullfil the time requirement     
    dp_time = [0 for i in range(max_time+1)]
    for i in range(n):
        for j in range(max_time, times[i]-1, -1):
            dp_time[j] = max(dp_time[j], dp_time[j-sizes[i]] + values[i])
    
   
    max_value = min(max(dp_size), max(dp_time)) # this would be the cap of the possible value
    if max_value == max(dp_size): 
        possible = list(filter(lambda num : num <= max_value, dp_time))
        return max(possible)
    elif max_value == max(dp_time):
        possible = list(filter(lambda num : num <= max_value, dp_size))
        return max(possible)
        
#dp_best_value(max_size, max_time, sizes, times, values)
#Out[76]: 8 
            
        
