# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:01:55 2018

@author: shuli
"""

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        while num != 1:
            if num % 2 == 0:
                num //= 2
            elif num %3 == 0:
                num //= 3
            elif num %5 == 0:
                num //= 5
            else:
                return False
        return True
    
if __name__ == '__main__':
    a = Solution()
    print(a.isUgly(-10))