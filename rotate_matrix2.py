#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:20:51 2020

@author: liwenhuang
rotation fast
"""

#/*
# * clockwise rotate
# * first reverse up to down, then swap the symmetry 
# * 1 2 3     7 8 9     7 4 1
# * 4 5 6  => 4 5 6  => 8 5 2
# * 7 8 9     1 2 3     9 6 3
#*/
#void rotate(vector<vector<int> > &matrix) {
#    reverse(matrix.begin(), matrix.end());
#    for (int i = 0; i < matrix.size(); ++i) {
#        for (int j = i + 1; j < matrix[i].size(); ++j)
#            swap(matrix[i][j], matrix[j][i]);
#    }
#}
#
#/*
# * anticlockwise rotate
# * first reverse left to right, then swap the symmetry
# * 1 2 3     3 2 1     3 6 9
# * 4 5 6  => 6 5 4  => 2 5 8
# * 7 8 9     9 8 7     1 4 7
#*/
#void anti_rotate(vector<vector<int> > &matrix) {
#    for (auto vi : matrix) reverse(vi.begin(), vi.end());
#    for (int i = 0; i < matrix.size(); ++i) {
#        for (int j = i + 1; j < matrix[i].size(); ++j)
#            swap(matrix[i][j], matrix[j][i]);
#    }
#}

# example input 
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def swap_symmetry(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]S
    
            

def clockwise(matrix):
    n = len(matrix)
    if n <= 1:
        pass
    matrix.reverse()
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    

def counter_clockwise(matrix):
    n = len(matrix)
    if n <= 1:
        pass
    
    for i in range(n):
        matrix[i].reverse()
    
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    

