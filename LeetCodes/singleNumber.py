# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 17:44:51 2018

@author: shuli
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for num in nums:
            try:
                hash_table.pop(num)
            except:
                hash_table[num] = 1
        return hash_table.popitem()[0]