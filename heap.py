# this is python implementation of maxheap
# insert and remove: O(logn), get max O(1)
# insert to the end, float up to the proper position, remove by swap top and last position, pop off last, float down the top, get to the parent node by index/2, get to left child by index*2, right child by index*2

class MaxHeap:
    def __init__(self, item = []):
        super().__init__()
        self.heap = [0] # 0 index position will not be used, but rather a placeholder
        for i in item:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1) # append new item and float them up to the proper position
    """
    @ take new data point, push into the heap
    """
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    """
    @return the root of the MaxHeap, return False when the heap is empty
    """
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    """
    @ return the root and maintain the heap structure
    three possibilities:
     1. there are more than two elements in the heap, swap the max with the last, pop off the last, float down the value at the top position
     2. only one element in the MaxHeap
     3. heap is empty
    """
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop(0)
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    """
    the internal floatUp function is recursive
    @ index of the node, starting with the end of the array
    """
    def __floatUp(self, index):
        parent = index//2
        if index <= 1: # already on top, do not need to do anything
            return
        elif self.heap[index] > self.heap[parent]: # swap if the node is larger than its parent
            self.__swap(index, parent)
            self.__floatUp(parent) # recurse until reach proper position

    """
    also called heapify, also a recursive function, does two comparison with its right and left node
    @ index of the node, starting with 1
    """
    def __bubbleDown(self, index):
        left = index*2
        right = index*2 + 1
        largest = index # note largest is a index not a value, assume new node at the right position
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index: # swap if the new node is not at the right position
            self.__swap(index, largest)
            self.__bubbleDown(largest)

# example code
m = MaxHeap([95, 3, 21])
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))
