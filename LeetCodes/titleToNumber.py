class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = ord(s[0]) - 64
        for alpha in s[1:]:
        	num = num * 26 + ord(alpha) - 64
        return num 
if __name__ == '__main__':
	a = Solution()
	s = 'AAA'
	print(a.titleToNumber(s))	  