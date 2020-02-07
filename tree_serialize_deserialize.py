#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:28:25 2020

@author: liwenhuang
tree serialize and deserialize
"""

#Input：{3,9,20,#,#,15,7}
#Output：{3,9,20,#,#,15,7}
#Explanation：
#Binary tree {3,9,20,#,#,15,7},  denote the following structure:
#	  3
#	 / \
#	9  20
#	  /  \
#	 15   7
#it will be serialized {3,9,20,#,#,15,7}

#Input：{1,2,3}
#Output：{1,2,3}
#Explanation：
#Binary tree {1,2,3},  denote the following structure:
#   1
#  / \
# 2   3
#it will be serialized {1,2,3}
                       
                       
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

        
    


class Solution:


    def serialize(self, root):
        if root is None:
            return "{}"

        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1

        while queue[-1] is None:
            queue.pop()

        return '{%s}' % ','.join([str(node.val) if node is not None else '#'
                                  for node in queue])


    def deserialize(self, data):
        data = data.strip('\n')

        if data == '{}':
            return None

        vals = data[1:-1].split(',')
            
        root = TreeNode(int(vals[0]))
        queue = [root]
        isLeftChild = True
        index = 0

        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if isLeftChild:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild

        return root