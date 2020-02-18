#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:39:41 2020

@author: liwenhuang
perfect square leetcode 279
https://leetcode.com/problems/perfect-squares/
given a number, return the minimum perfect squares that sum up the the given number
"""

"""
first dumb solution that exceed time limit
"""

def is_square(n):
    # input an int > 1
    for i in range(1, n+1):
        if i*i == n:
            return True
        
    return False

def perfect_square(n):
    # put all the square in a set for look up later
    square_set = set()
    for i in range(n+1):
        if is_square(i):
            square_set.add(i)
    #use a dict to cache all the number before n 
    dp = {}
    for i in range(1, n+1):
        if i <= 3:
            dp[i] = i
        if i in square_set:
            dp[i] = 1
    
    #populate all the previous number in the dp
    for i in range(5, n+1):
        if i not in dp:
            other_num = 0
            nn = i
            square_count = []
            while nn:
                nn -= 1
                other_num += 1
                if nn in dp and other_num in dp:
                    square_count.append(dp[nn] + dp[other_num])
            if square_count:
                dp[i] = min(square_count)
            else:
                dp[i] = i
    
    return dp[n]
                   
"""
try to optimize this dumb solution -- turns out to be still quite slow
"""
def perfect_square2(n):
    # put all the square in a set for look up later
    square_set = set()
    for i in range(n+1):
        if is_square(i):
            square_set.add(i)
    #use a dict to cache all the number before n 
    dp = {}
    for i in range(1, n+1):
        if i <= 3:
            dp[i] = i
        if i in square_set:
            dp[i] = 1
    
    #populate all the previous number in the dp, only need to check a few numbers
    for i in range(5, n+1):
        if i not in dp: # check all the square sets now
            potential_dp = []
            for j in square_set:
                if i > j: 
                    potential_dp.append(dp[j] + dp[i-j])
        
            if potential_dp:
                dp[i] = min(potential_dp)
            else:
                dp[i] = i
    return dp[n]

"""
try to optimize this dumb solution again, accepted but runtime is 5296 ms
"""
def perfect_square3(n):
    dp = [i for i in range(n+1)]
    for i in range(1, n+1):
        end = int(i**0.5)
        for j in range(1, end + 1):
            dp[i] = min(dp[i], dp[i - j*j] + 1)    
    return dp[n]


"""
using bfs in python would be faster, logic is very similar to shortest path problem 
""" 
def perfect_square_bfs(n):
    if n <= 3:
        return n 
    #stores all the squares in a set before n 
    square_set = []
    for i in range(1, n+1):
        if i*i <= n:
            square_set.append(i*i)
    
    # from this point on, break down the number of potential perfect square, each level consumes one perfect square
    to_check = {n}
    min_square = 0
    while to_check:
        min_square += 1
        temp = set() # the component of the perfect squares at this level will be the number to check at the next level
        for num in to_check:
            for square in square_set:
                if num == square: # the current number at the current level is a perfect square
                    return min_square
                if num < square: # no need to keep checking, eg, 5 is smaller than 9, we do not need to consider this case
                    break
                temp.add(num - square)
        to_check = temp
    
    return min_square
                
