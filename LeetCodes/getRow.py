# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:39:17 2018

@author: shuli
"""

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pre = [1]
        for row_num in range(rowIndex+1):
            row = [None for _ in range(row_num+1)]
            row[0] =1;row[-1] = 1
            for i in range(1,len(row)-1):
                row[i] = pre[i]+pre[i-1] 
            pre = row
        return row
#test
if __name__ == '__main__':
    a = Solution()
    print(a.getRow(0))