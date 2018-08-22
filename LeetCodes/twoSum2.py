# -*- coding: utf-8 -*-
"""
@author: lishulin
"""
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0;right = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
        	if numbers[left] + numbers[right] > target:
        		right -= 1
        	else: left += 1
        return [left+1,right+1]

if __name__ == "__main__":
	numbers = [2,7,11,15];target = 9
	a = Solution()
	print(a.twoSum(numbers,target))
