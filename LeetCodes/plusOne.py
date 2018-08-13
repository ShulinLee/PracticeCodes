# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 20:38:47 2018

@author: shuli
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == [0]:
            return 0
        flag = False
        for i in range(-1,-len(digits)-1,-1):
            if digits[i] == 9:
                digits[i] = 0
                flag = True
                continue
            else:
                break
        if flag:
            if digits[0] == 0:
                    digits.insert(0,1)
                    return digits
            else:
                digits[i-1] += 1
                return digits
        digits[-1] += 1    
        return digits