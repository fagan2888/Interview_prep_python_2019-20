#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:24:46 2020

@author: liwenhuang

matrix rotation 90 degree clockwise
"""

A = [[1,2,3],[4,5,6],[7,8,9]]

B = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

#output 
#[[7,4,1],
# [8,5,2],
# [9,6,3]]
# use this function to display the matrix
def displayMatrix(matrix): 
    n = len(matrix)

    for i in range(0, n):           
        for j in range(0, n): 
              
            print (matrix[i][j], end = ' ') 
        print ("") 

# dumbest solution copy each row then paste them as cols
def rotate_1(matrix):
    if not matrix:
        return None
    
    n = len(matrix)
    
    new_matrix = []
    for j in range(n):
        new_row = []
        for i in range(n):
            new_row.insert(0,matrix[i][j])
        new_matrix.append(new_row)
    
    return new_matrix
            
            
displayMatrix(A)
new_matrix = rotate_2(A)
displayMatrix(new_matrix)         

C = [[5]]
D = [[6, 7],[10,11]]

# rotate it layer by layer in-place, still pretty dumb, space use is not very efficient
# first_row => last col; last col => last row; last row = first col; first col => first row
#def rotate_2(matrix):
#    n = len(matrix)
#    first, last = 0, n-1
#    while first < last: # terminate when getting to the center of the matrix
#        first_row = [matrix[first][i] for i in range(first, last+1)] 
#        last_col = [matrix[i][last] for i in range(first, last+1)] # use list comprehension to extract all the element from this col
#        last_row = [matrix[last][i] for i in range(first, last+1)] 
#        first_col = [matrix[i][first] for i in range(first, last+1)]
#        # now repopulate the layer 
#        matrix[first:last] = [first_col.pop() for _ in range(first, last+1)]
#        matrix[last:last] = [last_col.pop() for _ in range(first, last+1)]
#        for i in range(first, last+1): # first and last col
#            matrix[i][last] = first_row.pop(0)
#            matrix[i][first] = last_row.pop(0)
#        
#        first += 1
#        last -= 1
#    
#    return matrix

    

# change one position at a time
def rotate_3(matrix):
    n = len(matrix)
    if n <= 1:
        return matrix
    
    for i in range(n):
        for j in range(n):
            matrix[j][n-1-i], matrix[i][j] = matrix[i][j], matrix[j][n-1-i]
    
    

# two steps swap
# first transpose the matrix, then swap all the cols
def rotate_4(matrix):
    if not matrix:
        return None
    n = len(matrix)
    if n == 1:
        return matrix
    
    new_matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]
    
    for i in range(n):
        first, last = 0, n-1
        while first != last: # condition needs to be rewritten 
            new_matrix[i][first], new_matrix[i][last] = new_matrix[i][last], new_matrix[i][first]
            first += 1
            last -= 1
    
    return new_matrix
            
    
   
    
