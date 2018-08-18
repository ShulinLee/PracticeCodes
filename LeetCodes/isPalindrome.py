# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 16:20:51 2018

@author: shuli
"""

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ''.join([ch for ch in s if ch.isalnum()]).lower()
        return new_s == new_s[::-1]

if __name__ == '__main__':
    a = Solution()
    s = "A man, a plan, a canal: Panama"
    print(a.isPalindrome(s))