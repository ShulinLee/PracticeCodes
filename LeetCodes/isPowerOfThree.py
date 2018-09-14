# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:13:11 2018

@author: shuli
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if n <= 0:
            return False
        epsilon = 0.001
        return (math.log10(n)/math.log10(3))%1 == 0
    
if __name__ == '__main__':
    a = Solution()
    print(a.isPowerOfThree(245))