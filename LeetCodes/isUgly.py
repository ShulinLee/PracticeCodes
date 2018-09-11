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
        while num %2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        return num == 1
    
if __name__ == '__main__':
    a = Solution()
    print(a.isUgly(-10))