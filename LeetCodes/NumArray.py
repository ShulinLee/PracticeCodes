# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:31:55 2018

@author: shuli
"""

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.dp = [0]
        result = 0
        
        for i in range(len(self.nums)):
            result += self.nums[i]
            self.dp.append(result)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1] - self.dp[i]
if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1]) 
    i,j = 0,5
    print(obj.sumRange(i,j))   