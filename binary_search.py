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
