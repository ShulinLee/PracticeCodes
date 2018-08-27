class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history = [];cur = n
        while (cur != 1) and (cur not in history):
        	cur = sum([int(num)**2 for num in str(cur)])
        	history.append(cur)
        return True if cur == 1 else False