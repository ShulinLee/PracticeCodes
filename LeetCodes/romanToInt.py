# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:07:36 2018

@author: shuli
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        prefix = 0
        current_val = 0
        for i in range(len(s)-1,-1,-1):
            current_val = table[s[i]]
            if current_val < prefix:
                result -= table[s[i]]
            else:
                result += table[s[i]]
            prefix = current_val
        return result
            
if __name__ == '__main__':
    a = Solution()
    print(a.romanToInt(''))