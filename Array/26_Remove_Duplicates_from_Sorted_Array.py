"""
26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the new length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            max = nums[len(nums)-1]
            min = nums[0]
            length = 0
            k = 0
            for i in range(min,max+1):
                if i in nums:
                    length +=1
                    nums[k] = i
                    k += 1
            nums = nums[:length]
            return length


x = Solution()
x.removeDuplicates([1,1,2,3,5,5,6])
print(x.removeDuplicates([1,1,2,3,5,5,6]))