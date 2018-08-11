# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 18:27:44 2018

@author: shuli
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        left = 0;right = len(nums) - 1
        while left < right:
            mid = (right+left)//2
            if target > nums[mid]:
                left = mid +1
            else:right = mid -1
        return left if nums[left] > target else left+1

if __name__ == '__main__':
    a = Solution()
    nums = [1,3,5,6];targetList = [5,2,7,0]
    for target in targetList:
        print(a.searchInsert(nums,target))