class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = abs(n)
        while n>1:
        	if n%2 != 0:
        		return False
        	n //= 2
        return n!=0