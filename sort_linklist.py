#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:36:49 2020

@author: liwenhuang
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#append all the nodes in a list
def sort_linklist(head):
    if not head:
        return None
    
    node_list = []
    while head:
        node_list.append(head)
        head = head.next

    # sort the list to the node values, here use any sorting algorithm
    new_list = sorted(node_list, key = lambda node: node.val)
    print(new_list)
    # return a sorted new linkList
    dummy = new_head = ListNode(0)
    while new_list:
        current_node = new_list.pop(0)
        #print(current_node.val)
        new_head.next = current_node
        new_head = new_head.next
    new_head.next = None # avoid cycle
    
    return dummy.next


    
