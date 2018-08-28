class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #不包括n本身
        if n < 3:
        	return 0
        #构造一个指示列表，0、1不是质数，所以为0
        indictList = [0,0]+[1]*(n-2)
        #构造的列表从0开始，到n-1，即数字和索引一致
        for num in range(2,int(n**0.5)+1):
        	if indictList[num]:
        		#将num的倍数置为0
        		indictList[num**2:n:num] = [0]*len(indictList[num**2:n:num])
        return sum(indictList)