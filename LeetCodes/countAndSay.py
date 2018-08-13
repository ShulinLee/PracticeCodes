# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 19:12:37 2018

@author: shuli
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        def readStr(s):
            if s == '1':
                return '11'
            temp = s[0]
            count = 1
            result = ''
            for i in range(1,len(s)):
                if i == len(s) - 1:
                    if s[i] == temp:
                        count += 1
                        result += str(count)+temp
                    else:
                         result += str(count)+s[i-1]+'1'+s[i]   
                else:
                    if s[i] == temp:
                        count += 1
                    else:
                        result += str(count)+temp
                        count = 1
                        temp = s[i]
            return result
        
        def recursion(n):
            if n == 1:
                return '1'
            return readStr(recursion(n-1))
    
        final = recursion(n)
        return final
                    
if __name__ == '__main__':
    a = Solution()
    print(a.countAndSay(6))