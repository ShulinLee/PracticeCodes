import pdb
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	binstr = lambda m: '' if m == 0 else str(m%2) + binstr(m//2)
    	if len(binstr(n)) < 32:
    		target = binstr(n) + (32 - len(binstr(n))) * '0'
    	else: target = binstr(n)
    	result = 0
    	for num in target:
    		result = result * 2 +  int(num)
    	return result

if __name__ == "__main__":
	a = Solution()
	print(a.reverseBits(43261596))