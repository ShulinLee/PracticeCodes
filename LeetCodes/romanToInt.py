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
        num = 0;err = 0
        s1 = s + 'I'
        for i in range(len(s)):
             if (s1[i] == 'I' and ((s1[i+1] == 'V') or(s1[i+1] == 'X'))) or (s1[i] == 'X' and ((s1[i+1] == 'L') or (s1[i+1] == 'C'))) or (s1[i] == 'C' and ((s1[i+1] == 'D') or (s1[i+1] =='M'))):
                        num += (table[s1[i+1]] - table[s1[i]])
                        err += table[s1[i+1]]
             else: 
                 num += table[s[i]]               
        return num-err
if __name__ == '__main__':
    a = Solution()
    print(a.romanToInt('MCMXCIV'))