# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:38:21 2018

@author: shuli
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            row[0] = 1;row[-1] = 1
            for j in range(1,len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            triangle.append(row)
        return triangle
    
#test
if __name__ == '__main__':
    a = Solution()
    print(a.generate(0))