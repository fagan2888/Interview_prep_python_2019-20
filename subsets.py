#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:10:24 2020

@author: liwenhuang
the subset problem : the classic four solution
"""

nums = [1, 2, 3]

"""
Subset problems are doable with BFS, the problem is the space complexity
Observe the following two ways in implement BFS, imagine drawing these two search trees in the head or on a piece of paper
1. add one member to the last step, contrain on the added member should follow certain order otherwise repetition will occur
2. in each step, ask if the a new member should be added, the iteration stop when looping through all memerbers in the set
"""

# implement the first bfs idea
# any single subset generated in the process is one member in the return

def subsetBfs1(nums):
    subsets = [[]]
    last_layer = [[]]
    new_layer = []

    while len(subsets) < 2**(len(nums)):# THe maximum subsets that can be achieved
        for subset in last_layer:
            for num in nums:
                if len(subset) == 0 or num > subset[-1]: # add this contraint to avoid repetition
                    new_subset = subset + [num]
                    new_layer.append(new_subset)
        subsets.extend(new_layer)
        last_layer = new_layer
        new_layer = []

    return subsets

# implement the second bfs idea
# reach the return result in the last layer, note that this solution also don't care about order

def subsetBfs2(nums):
    last_layer = [[]]
    new_layer = []
    for num in nums: # loop through all members in the set
        print('num', num)
        print('last_layer',last_layer)
        for subset in last_layer:
            new_layer.append(subset)
            new_subset = subset + [num]
            new_layer.append(new_subset)
            print('new_layer', new_layer)
        last_layer = new_layer
        new_layer = []

    return last_layer

# or you can express this idea in a recursion, note that this solution does not take care of order
def subsetBfs2_recursion(nums):
    if len(nums) == 0:
        result = [[]]
    elif len(nums) == 1:
        result =[[], nums]

    else:
        new_layer = []
        last_layer = subsetBfs2_recursion(nums[:-1])
        for subset in last_layer:
            new_subset = subset + [nums[-1]]
            new_layer.append(new_subset)
        last_layer.extend(new_layer)

        result = last_layer

    return result

# a way more elegant implementation
class Solution:

    def subsets(self, nums):

        nums.sort()
        output = [[]]

        for num in nums:
            output.extend([subset + [num] for subset in output])

        return output

"""
Fortunately, this two BFS can be easily adapted to DFS
"""
class Solution1:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        nums = sorted(nums)
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations

    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()


class Solution2:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        result_sets = []
        self.dfs(num, 0, [], result_sets, target)
        return sorted(result_sets)

    def dfs(self, num, idx, current_elements, result_sets, target):
        if sum(current_elements) == target and sorted(current_elements) not in result_sets:
            result_sets.append(list(sorted(current_elements)))

        for i in range(idx, len(num)):
            current_elements.append(num[i])
            self.dfs(num, i+1, current_elements, result_sets, target)
            current_elements.pop()


num = [7,1,2,5,1,6,10]
target = 8

ans = Solution()
ans.combinationSum2(num, target)
