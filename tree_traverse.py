#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:46:16 2020

@author: liwenhuang
different tree traversal 
"""

#	  3
#	 / \
#	9  20
#	  /  \
#	 15   7
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

"""
print out all the node values in level order
[3, 9, 20, 15, 7]
"""

def print_all_values(root):
    if not root:
        return []
    
    q = [root]
    result = []
    while q:
        current_node = q.pop(0)
        result.append(current_node.val)
        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)
    
    return result
    


"""
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

same as you would with level traverse, but use insert(0, new_list) instead 
"""
def levelOrderBottom(root):
        if not root:
            return []
        
        q = [root]
        result = []
        while q:
            level_result = []
            for _ in range(len(q)):
                current_node = q.pop(0)
                level_result.append(current_node.val)
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            result.insert(0, level_result)
        
        return result


"""
print all the node values 
[3, 9, #, #,20, 15, 7]
"""

def print_node_val(root):
    if not root:
        return []
    
    q = [root]
    result = []
    while q:
        for _ in range(len(q)):
            current_node = q.pop(0)
            if current_node is not None:
                result.append(current_node.val)
                q.append(current_node.left)
                q.append(current_node.right)
            else:
                result.append('#')
            
    
    while result[-1] == '#':
        result.pop()
    
    return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    