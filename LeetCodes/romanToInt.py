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
        i = 0;result = 0
        matches = {('I','V'),('I','X'),('X','L'),('X','C'),('C','D'),('C','M')}
        while i < len(s) -1:
            if (s[i],s[i+1]) in matches:
                result += table[s[i+1]] - table[s[i]]
                i += 2
            else:
                result += table[s[i]]
                i += 1
        if i == len(s) -1:
            result += table[s[-1]]
        return result
if __name__ == '__main__':
    a = Solution()
    print(a.romanToInt('MCMXCIV'))