class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x = x
        flag = 1
        if self.x >= 10:
            length = len(str(self.x))
        elif self.x >= 0:
            return self.x
        else:
            length = len(str(self.x))-1
            self.x = -self.x
            flag = -1
        a = []
        for i in range(length-1,-1,-1):
            a.append((self.x%10)*(10**i))
            self.x = self.x//10
        revNum = flag*sum(a) 
        if revNum >= -2**31 and revNum <= 2**31-1:
            return revNum
        else: return 0
if __name__ == '__main__':
    a = Solution()
    