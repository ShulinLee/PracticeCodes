class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        maximum = 0
        for num in nums:
        	dic[num] = dic.get(num,0) + 1
        	if dic[num] > maximum:
        		maximum = dic[num]
	        	if maximum > len(nums) // 2:
	        		return num

if __name__ == '__main__':
	a = Solution()
	nums = [1]
	print(a.majorityElement(nums))	   