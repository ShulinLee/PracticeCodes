# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:27:02 2018

@author: shuli
"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        for i in range(len(nums)+1):
            if i not in num_set:
                return i
if __name__ == '__main__':
    a = Solution()
    nums = []
    print(a.missingNumber(nums))