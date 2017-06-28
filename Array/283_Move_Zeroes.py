"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(0,len(nums)):
            if nums[i] != 0 :
                nums[j] = nums[i]
                j += 1
        for k in range(j,len(nums)):
            nums[k] = 0

        print(nums)

x = Solution()

y = x.moveZeroes([0, 1, 0, 3, 12, 11, 111, 0, 0])
