#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:45:32 2020

@author: liwenhuang
implement trie in python
https://leetcode.com/problems/implement-trie-prefix-tree/
https://www.interviewcake.com/concept/java/trie
"""

class Trie:
    head = {}
    
    def insert(self, word):
        # move the pointer to the dictionary within a dictionary, layer by layer and layer
        cur = self.head
        
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur["*"] = True # this signal the end of a word

    def search(self, word):
        # traverse node by node until see "*" at the end
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            else:
                cur = cur[ch]
        return "*" in cur
    
    def startWith(self, prefix):
        cur = self.head
        for ch in prefix:
            if ch not in cur:
                return False
            else:
                cur = cur[ch]
        return True



t = Trie()
t.insert("apple")
#Out[44]: True
t.search("apple")
t.startWith("app")
#Out[43]: True

