# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:40:05 2018

@author: shuli
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = x
        if self.x<0 or (x%10==0 and x!=0):
            return False
        else:
            revNum = 0
            while(self.x > revNum):
                revNum = revNum*10+self.x%10
                self.x = self.x//10
            return revNum == self.x or revNum//10 == self.x
                
if __name__ == '__main__':
    a = Solution()
