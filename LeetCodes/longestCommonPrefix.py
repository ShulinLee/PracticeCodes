# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:59:24 2018

@author: shuli
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        result = []
        for i in range(min([len(s) for s in strs])):
            if len({a[i] for a in strs}) != 1:
                break
            result.append(strs[0][i])
        return ''.join(result)
                
if __name__ == '__main__':
    a = Solution()
    s = ["a","a","aabc","aa","acc",'']
             