# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:41:53 2018

@author: shuli
"""

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split(' ')
        if len(pattern) != len(strList):
            return False
        lookup = {}
        for i in range(len(pattern)):
            if pattern[i] in lookup:
                if strList[i] == lookup[pattern[i]]:
                    continue
                else:return False
            else:
                if strList[i] in lookup.values():
                    return False
                else:lookup[pattern[i]] = strList[i]
        return True
    
if __name__ == '__main__':
    a = Solution()
    pattern = 'abba'
    str = 'dog dog dog dog'
    print(a.wordPattern(pattern,str))