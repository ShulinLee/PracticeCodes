# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 10:58:12 2018

@author: shuli
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else: i += 1
        return len(nums)
if __name__ == '__main__':
    a = Solution()
    nums = [0,1,2,2,3,0,4,2];val = 2
    print(a.removeElement(nums,val))
    