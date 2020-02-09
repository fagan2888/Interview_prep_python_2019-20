#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:50:49 2020

@author: liwenhuang

all the pointer manipulation you can imagine
just remember in linkedlist store data very differently than array(former scatterd while latter always at the same location), node has data and the next position
manipulation usually requires knowing the previous position on top of the current position
manipulation on a node involves chagning all the connections
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
#node.next.next.next.next = ListNode(5)

#use the following function to print all node vals
while node:
    print(node.val)
    node = node.next


"""
add one node to the linkedlist
"""
def insert_end(node, key):
    if not node:
        node = ListNode(key)
    else:
        last_node = node
        while last_node.next!= None: # traverse to the last node of the list
            last_node = last_node.next
        last_node.next = ListNode(key)
    
    return node

def insert_head(node, key):
    if not node:
        node = ListNode(key)
    else:
        temp_node = node
        head = ListNode(key)
        head.next = temp_node
    
    del temp_node
    return head

def insert_position(head, new_node, n):
    if n == 0:
        new_node.next = head
        return new_node  
    
    position = 0 # starting from the head node, which has position 0
    cur_node = head
    while True:
        if position == n:
            pre_node.next = new_node
            new_node.next = cur_node
            break
        pre_node = cur_node #store the current node as the previous node
        position += 1
        cur_node = cur_node.next
    
    return head
    
       
"""
this is how to delete a node with certain value
node = node.next is only moving the pointer
"""
def deleteNode(head, key):
    if not head:
        return None
    if head.val == key: # key is the head
        head = head.next
    else:
        pre_node, cur_node = head, head.next
        while cur_node.next != None: # key is not at the end of the list
            if cur_node.val == key:
                pre_node.next = cur_node.next
            pre_node = pre_node.next
            cur_node = cur_node.next
        
        if cur_node.val == key:#last node
            pre_node.next = None
    
    return head
    

"""
24. Swap Nodes in Pairs
Given 1->2->3->4, you should return the list as 2->1->4->3.

have a dummy node = cur, make it point to the head node, the next order of change is important
1. cur.next = 2nd
2. 1st.next = 2nd.next
3. 2nd.next = 1st
"""

def swapPairs(head):
    dummy = cur = ListNode(0)
        
    cur.next = head
    while cur.next and cur.next.next:
        first, second = cur.next, cur.next.next
        cur.next = second
        first.next = second.next
        second.next = first
        cur = cur.next.next
        
    return dummy.next


"""
swap two nodes, consider if one of them is the head node, or the two nodes are adjacent
"""

def swap_node(head, x, y):
    if x == y: # when the values are the same, no swapping is neccessary
        return 
    
    #search x and y, does not consider if one is head or the two nodes are adjacent
    cur_node = head    
    while cur_node:
        if cur_node.val == x:
            x_node = cur_node
            pre_x = pre_node
        if cur_node.val == y:
            y_node = cur_node
            pre_y = pre_node        
        pre_node = cur_node
        cur_node = cur_node.next
    # do the swap
    pre_x.next, pre_y.next = y_node, x_node
    x_node.next, y_node.next = y_node.next, x_node.next
    
"""
reverse a linkedlist in-place
""" 
   

prev = None
while node:
    node.next, prev, node = prev, node, node.next
node = prev

while node:
    print(node.val)
    node = node.next

# 1 -> 2



