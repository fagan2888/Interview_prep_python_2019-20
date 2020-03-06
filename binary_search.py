#binary search

nums = [9, 4, 2, 3, 7, 1]

def binary_search(nums, target):
    if not nums:
        return False

    nums.sort()
    n = len(nums)
    mid = n//2
    if nums[mid] == target:
        return True
    elif nums[mid] < target:
        return binary_search(nums[mid+1:], target)
    else:
        return binary_search(nums[:mid], target)

    return False


"""
although the above method would work, but binary search is not a typiclal recuisive Solution
the following is the jiuzhang template
start + 1 < end
mid = start + (end - start) //2 (in python there is no such thing as stackoverflow but nice to watch out for other languages)
A[mid] ==, <, > A[start] A[end] ? target
try the following solution to find the last occurance of a target number
"""

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        if not A or target is None:
            return -1

        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        else:
            return -1
