class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
 		lookup = {}
 		while n != 1 and n not in lookup:
 			lookup[n] == True
 			n = sum([int(num)**2 for num in str(n)])
 		return n == 1