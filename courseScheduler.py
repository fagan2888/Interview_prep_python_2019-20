#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:45:36 2020

@author: liwenhuang

course scheduler
Input: n = 2, prerequisites = [[1,0],[0,1]] 
Output: false

this is a implicit graph prolem, this is how to think about this problem and similar problems of detecting cycle in a graph
1. build the graph and the array to keep track of the changes of in-degrees
2. put all the node with 0 in-degree into a q, process them by removing 1 in-degree for all of their neigbor nodes
3. you won't be able to return a topographical sort order if there is a cycle
"""
n = 1
prerequisites = [[1,0]] 

def canFinish(n, prerequisites):
    # build the graph and in-degree array
    graph = {i:[] for i in range(n)}
    in_degrees = [0 for i in range(n)] 
    
    for i, j in prerequisites:        
        graph[j].append(i)
        in_degrees[i] += 1
    
    q, counter = [], 0
    
    # extract the 0 in-degree and process them in a q
    for i in range(n):
        if in_degrees[i] == 0:
            q.append(i)
    
    while q:
        current_node = q.pop(0)
        counter += 1
        for neigbor_node in graph[current_node]:
            in_degrees[neigbor_node] -= 1
            if in_degrees[neigbor_node] == 0:
                q.append(neigbor_node)
    
    return counter == n 
