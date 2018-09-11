# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:46:27 2018

@author: shuli
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,count = 0,0
        while i < len(nums) - count:
            if nums[i] == 0:
                del nums[i]
                nums += [0]
                count += 1
            else:
                i += 1
if __name__ == '__main__':
    a = Solution()
    nums = [0,1,0,3,12,0,8]
    a.moveZeroes(nums)
