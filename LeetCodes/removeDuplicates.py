# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:55:47 2018

@author: shuli
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        trail = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[trail]:
                trail += 1
                nums[trail] = nums[i]
        return trail+1
    
if __name__ == '__main__':
    a= Solution()
    s = [1,2,2,3,3,3,4,4,6]
    print(a.removeDuplicates(s))
            