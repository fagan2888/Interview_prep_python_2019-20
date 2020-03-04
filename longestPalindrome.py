#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:25:45 2020

@author: liwenhuang

Longest Palindromic Substring

Input:"abcdzdcab"
Output:"cdzdc"

The brute force solution (evaluate each substring, moving two pointers forward) has O(n^3) complexity
DP solution reduce it to O(n^2) but hard to understand
The best solution is numerate from the middle, O(2n -1)*n/2, still O(n^2)
The only O(n) solution is Manacher's Algorithm

"""

s = "abcdzdcab"

def longestPalindrome(s):
    if not s:
        return ''
    
    start, longest = 0, 0
    n = len(s)
    for middle in range(n):
        # odd length situation
        left, right = middle, middle
        while left >= 0 and right < n and s[right] == s[left]:
            left -= 1
            right += 1
            current_length = right - left - 1 # this is the length we have checked
            if current_length > longest: 
                longest = current_length
                start = left + 1 # note that we have not check the updated right and left yet
        
        # the even length situation
        left, right = middle, middle+1
        while left >= 0 and right < n and s[right] == s[left]:
            left -= 1
            right += 1
            current_length = right - left - 1
            if current_length > longest:
                longest = current_length
                start = left + 1
    
    return s[start:start + longest]
                
    

#### the above solution can be simply to
def longestPalindrome_s(s):
    longest = ''
    n = len(s)
    
    def numerate_from_middle(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left+1:right]
    
    for middle in range(n):
        sub = numerate_from_middle(s, middle, middle) # the odd length
        if len(sub) > len(longest):
            longest = sub
        sub = numerate_from_middle(s, middle, middle+1) # the even length
        if len(sub) > len(longest):
            longest = sub
    return longest
        
    

    