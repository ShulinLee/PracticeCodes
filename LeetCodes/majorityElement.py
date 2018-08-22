class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt,majority = 0,None
        for num in nums:
        	if cnt == 0:
        		majority = num
        	if majority == num:
        		cnt += 1
        	else:
        		cnt -= 1
        return majority

if __name__ == '__main__':
	a = Solution()
	nums = [1]
	print(a.majorityElement(nums))	   