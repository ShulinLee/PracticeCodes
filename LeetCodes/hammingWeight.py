class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        str = "{0:b}".format(n)
        return sum([int(num) for num in str])