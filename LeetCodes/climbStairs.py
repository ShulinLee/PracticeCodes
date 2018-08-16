# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 12:10:10 2018

@author: shuli
"""

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        for _ in range(n):
            a,b = b,a+b
        return b
if __name__ == '__main__':
    a = Solution()
    print(a.climbStairs(35))