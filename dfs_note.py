#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:35:25 2020

@author: liwenhuang

Note on doing dfs, there are in general two approaches, considered which works best for the situation
1. have a global variable, update this glocal variable at each step, no return argument
2. use a local argument, update this argument when passing into the function for the next step, set return condition
"""

#situation one : get the total number of nodes in a binary tree
class CountNode:
    def countNode(self, root):
        self.count = 0
        self.dfs(root, self.count)
        return self.count
    
    def dfs(self, node):
        if node:
            self.count += 1
        
            self.dfs(node.left)
            self.dfs(node.right)
        else:
            return 

# situation two, choose k number from an array so that the sum is a prime number
# a=[3,7,12,19]，k=3 answer is 3+7+19＝29

            
class Solution:
    """
    @param a: the n numbers
    @param k: the number of integers you can choose
    @return: how many ways that the sum of the k integers is a prime number
    """
    def getWays(self, a, k):
        ans = []
        self.search(a, k, [], ans)
        return ans
 
    
    def search(self, arr, k, combo, combos):
        if k == 0:
            combo_sum = sum(combo)
            if self.is_prime(combo_sum):
                combos.append(list(combo))        
            return 
        
        n = len(arr)
        for i in range(n):
            #combo.append(arr[i])
            self.search(arr[i+1:], k-1, combo + [arr[i]], combos)
            #combo.pop()
        
    def is_prime(self, n):
        for i in range(n//2):
            if n % 2 == 0:
                return False
        
        return True

    
"""
Note that in the situation 2, there are 2 keys
1. when update he result, in this case, the final set 'ans' to be return at last, apply deep copy of the result for each path
This can be accomplish by [:] or list in python, otherwise, the variable combo should change as the function goes on
2. it is important to update the combo argument to combo + [arr[i]] at each step, line 55 can also be accomplished by line54 and 56
using a pop() function
"""
