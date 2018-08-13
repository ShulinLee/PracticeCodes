# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:52:21 2018

@author: shuli
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        maximum = nums[0];curSum = nums[0]
        for num in nums[1:]:
            curSum = max(curSum+num,num)
            maximum = max(curSum,maximum)
        return maximum