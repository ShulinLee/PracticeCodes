# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 20:09:02 2018

@author: shuli
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        strs = [a for a in s.split(' ') if a != '']
        return len(strs[-1]) if len(strs) != 0 else 0