# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 16:26:30 2018

@author: shuli
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        (short,long) = (a,b) if len(a) < len(b) else (b,a)
        short = (len(long) - len(short))*'0' + short
        i = -1
        temp = 0
        while -i <= len(long):
            if int(short[i]) + int(long[i]) + temp >= 2:
                result = str((int(short[i]) + int(long[i]) + temp)%2) + result
                temp = 1
            else:
                result = str(int(short[i]) + int(long[i]) + temp) + result
                temp = 0
            i -= 1
        return str(temp) + result if temp == 1 else result    

if __name__ == '__main__':
    a = Solution()
    print(a.addBinary('11001','111010'))          