# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 17:28:19 2018

@author: shuli
"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        left,right = 1,x
        while left < right:
            mid = (left + right) // 2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                left = mid + 1
            else:
                right = mid
        return left if left**2 == x else left -1
                