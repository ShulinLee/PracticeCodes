class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            temp = 0
            for i in str(num):
                temp += int(i)
            num = temp
        return num
    
if __name__ == '__main__':
    a = Solution()
    print(a.addDigits(38))