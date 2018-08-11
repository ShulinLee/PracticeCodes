# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 17:47:53 2018

@author: shuli
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        index = -1
        for i in range(0,len(haystack)-len(needle)+1):
            if needle[0] ==  haystack[i]:
                if haystack[i:i+len(needle)] == needle:
                    index = i
                    break
        return index
    
if __name__ == '__main__':
    a = Solution()
    haystack = 'aaaaa';needle = 'bba'
    print(a.strStr(haystack,needle))
        
                    