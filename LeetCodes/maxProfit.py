# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 15:31:08 2018

@author: shuli
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = 1000000000;maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif (price - minprice) > maxprofit:
                maxprofit = price - minprice
        return maxprofit
            
    
if __name__ == '__main__':
    a = Solution()
    prices = [7,6,4,3,1]
    print(a.maxProfit(prices))