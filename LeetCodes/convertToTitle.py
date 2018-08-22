class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 27:
        	return chr(n+64)
        result = ''
        while n >26:
        	result = chr((n-1)%26 +65) + result
        	n = (n-1) // 26 
        return chr(n+64) + result

if __name__ == '__main__':
	a = Solution()
	print(a.convertToTitle(701))