#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:49:42 2020

@author: liwenhuang
word ladder problem 1 & 2
"""

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

"""first build a hash map of all the interwords, there are two ways to go about it
   use permutation to compuate the distance between words, interwords are the one that are one character in diff"""

wordList.append(beginWord)
from collections import defaultdict

#use permutation
inter_dict = defaultdict(set)
for word in wordList:
    for i in range(len(word)):
        for char in "abcdefghijklmnopqrstuvwsyz":
            new_word = word[:i] + char + word[i+1:]
            if new_word in wordList:
                inter_dict[word].add(new_word)
    inter_dict[word] -= {word}

# find strings that is one character difference 1[away, note that we can do this only as we know all the strings are of the same len
def diff_1(w1, w2):
    n = len(w1)
    boo_vect = [w1[i] == w2[i] for i in range(n)]
    if sum(boo_vect) == n - 1:
        return True
    else:
        return False

inter_dict2 = defaultdict(set)
for w1 in wordList:
    for w2 in wordList:
        if diff_1(w1, w2):
            inter_dict2[w1].add(w2)

# use a q to record the level it takes to get to the end word, use a set to remember what are the visited words
visited = set()
q = [beginWord]
visited.add(beginWord)
all_seqs = [[]] # the ladder starts with the beginWord

level = 1 # the beginword is counted as the first step
while q:
    level += 1
    combo = [] # use this to store all the current_words in the same level in the q
    temp = []
    for _ in range(len(q)):
        current_word = q.pop()
        for inter_word in inter_dict[current_word]:
            if inter_word == endWord:
                print('found!', level, current_word, inter_word)
                for i in range(len(all_seqs)):
                    all_seqs[i].append(current_word)
                    all_seqs[i].append(inter_word)
                    print(all_seqs[i])
                    break
            else:
                if inter_word not in visited:
                    visited.add(inter_word)
                    q.append(inter_word)
        
        combo.append(current_word)
        #print("this is what are in the combo:", combo)
    for word in combo: 
        for seq in all_seqs:
            new_seq = seq + [word]
            temp.append(new_seq)
    all_seqs = temp
    
#found! 4 log cog
#['hit', 'hot', 'log', 'cog']
#found! 5 dog cog
#['hit', 'hot', 'log', 'cog', 'lot', 'dog', 'cog']      
      

    
                    
                    
            

        

    
    
