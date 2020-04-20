"""
 bubble sort
"""
# keep a flag to indicate whether the array is sorted
#-- way to optimize is to remember each sweep push the largest element to the end of the array
def bubble_sort(nums):
    n = len(nums)-1
    is_sorted = False
    while is_sorted == False:
        is_sorted = True
        for i in range(n):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                is_sorted = False
        print(nums)
        n -= 1


"""
 theoretically merge sort is awesome for its perfect divide and conquer logics, no matter what happens it remains nlogn, but the disavantage is the O(n) extra space that is requires to do the merging
 whenever a new array needs to be created and released, that takes up resources, therefore, in practice, quicksort may be actually better
 a slight optmization for merge sort can be passing an array into the function as a parameter therefore the operation of creating a new array dose not need to be done multiple times
 the following solution modify the original array instead, however, note that it dose not save the O(n) space
"""
nums = [5, 2, 7, 9, 20, 1]
# merge sort

def merge_sort(nums):
    if len(nums) == 1:
        return
    mid = len(nums)//2
    left, right = nums[:mid], nums[mid:] # O(n) space
    merge_sort(left)
    merge_sort(right)

    # modify the original nums array
    k = 0
    while left and right:
        if left[0] < right[0]:
            nums[k] = left.pop(0)
        else:
            nums[k] = right.pop(0)
        k += 1
    while left:
        nums[k] = left.pop(0)
        k += 1
    while right:
        nums[k] = right.pop(0)
        k += 1


"""
归并排序算法的步骤为：

找出数组的中点
将数组分成两个部分递归执行该算法，分别排序两个部分
合并两个排序好的子数组到一个大数组
写成T函数为：T(n) = 2*T(n/2) + O(n)T(n)=2∗T(n/2)+O(n)，其中

2*T(n/2)2∗T(n/2) 代表将 n 的问题，拆分为两个 n/2 的同类问题去进行处理。
O(n)O(n) 代表了，合并两个排好序的 n/2 大小的数组的时间复杂度。
我们用展开的方式推导该算法下的 T(n):

T(n) = 2 * T(n/2) + O(n)
     = 2 * (2 * T(n/4) + O(n/2)) + O(n)
     = 4 * T(n/4) + 2 * O(n/2) + O(n)
     = 4 * T(n/4) + 2 * O(n)
     = 4 * (2 * T(n/8) + O(n/4)) + 2 * O(n)
     = 8 * T(n/8) + 3 * O(n)
     = 16 * T(n/16) + 4 * O(n)
     ...
     = n * T(1) + logn * O(n)
     = O(n) + O(nlogn)
     = O(nlogn)
"""


"""
quick sort is pretty difficult for me to remember in details for some reasone, here I use the following dumb implementation to learn its logic
"""
def quick_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums

    pivot = nums.pop() # can assign the pivot using other ways, but this can do the assignment and remove at one go

    lower = []
    higher = []
    for num in nums:
        if num < pivot:
            lower.append(num)
        else:
            higher.append(num)

    return quick_sort(lower) + [pivot] + quick_sort(higher)

# here is the implementation of quicksort
class Solution:
    def sort(self, nums):
        self.quick_sort(nums, 0, len(nums)-1)

    def quick_sort(self,nums, start, end):
        if start >= end:
            return

        pivot = nums[(start+end)//2]
        left, right = start, end

        while left < right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left < right:
                nums[left], nums[right] =  nums[right], nums[left]
                left += 1
                right -= 1

        # the position of the index: right before left
        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)


nums = [5, 2, 7, 9, 20, 1]
ans = Solution()
ans.sort(nums)

"""
although quick sort build on top of quick select, the partition part is identical, but for some reason, it is really difficult to do it right, especially remember the right portion
here is a template for me to remember
note the different condition when using left < right or left <= right in the implementation, that result in different final positions of the left and right pointers
"""
# quick select, solve problem such as k-th element, find median, O(n) averaged time complexity
def quick_select(nums, k, start, end):
    if start == end:
        return nums[start]

    left, right = start, end
    pivot = nums[(start + end)//2]
    while left <= right:
        while nums[left] < pivot:
            left += 1
        while nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    if start + (k-1) <= right:
        return quick_select(nums, k, start, right)
    if start + (k-1) >= left:
        return quick_select(nums, k - (left-start), left, end)
    return pivot

quick_select(nums, 1, 0, len(nums)-1)
