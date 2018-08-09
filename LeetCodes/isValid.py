# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 10:25:09 2018

@author: shuli
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        opening = ['(','[','{']
        matches = [('(',')'),('[',']'),('{','}')]
        stack = []
        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if stack == []:
                    return False
                last_open = stack.pop()
                if (last_open,paren) not in matches:
                    return False
        return stack == []
    