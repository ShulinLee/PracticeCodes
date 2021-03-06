# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 16:11:04 2018

@author: shuli
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                maxprofit += prices[i+1] - prices[i]
        return maxprofit
