"""
Given a sorted array and a target value, return the index if the target is found.

If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        elif nums[0]>target:
            return 0
        elif nums[-1]<target:
            return len(nums)
        else:
            for i in nums:
                if i < target and nums[nums.index(i)+1] > target:
                    return nums.index(i)+1


x = Solution()
print(x.searchInsert([1,3,5,6],4))
