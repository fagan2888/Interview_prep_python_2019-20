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


# merge two sorted lists
nums1 =[2, 7, 9, 11, 15]
nums2 =[2, 4, 5]

def merge(nums1, nums2):
    arr = []
    while nums1 and nums2:
        if nums1[0] <= nums2[0]:
            num = nums1.pop(0)
        else:
            num = nums2.pop(0)
        arr.append(num)

    if nums1:
        arr.extend(nums1)
    if nums2:
        arr.extend(nums2)

    return arr

# merge two sorted array in place
nums1 = [1,2,3]
m = 3
nums2 = [2,5,6]
n = 3

def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for num in nums2:
            for i in range(m):
                if nums1[i] <= num:
                    left = i
                if nums1[i] >= num:
                    right = i
            if left:
                nums1.insert(left+1, num)
            else:
                nums1.insert(right-1, num)
            print(nums1)
            m += 1

#merge(nums1, m, nums2, n)

# merge two sorted linklist
# use recursion
def mergeTwoLists2(l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2

# return a new list
def mergeTwoLists(l1, l2):

    dummy = pointer = ListNode(0)

    while l1 and l2:
        if l1.val <= l2.val:
            pointer.next = l1
            l1 = l1.next
        else:
            pointer.next = l2
            l2 = l2.next
        pointer = pointer.next

    pointer.next = l1 or l2

    return dummy.next

"""
 merge sort in a dumb way
"""
nums = [7, 8, 10, 5, 9, 7, 2]

def merge_sort(nums):
    def merge(nums1, nums2):
        arr = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                num = nums1.pop(0)
            else:
                num = nums2.pop(0)
            arr.append(num)

        if nums1:
            arr.extend(nums1)
        if nums2:
            arr.extend(nums2)

        return arr

    n = len(nums)
    if n <= 1:
        return nums
    mid = n//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


# solution from geekforgeek
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1



"""
quick sort in a dumb way
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


Sa
