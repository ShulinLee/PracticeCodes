class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > 0 and nums != []:
        	nums.insert(0,nums[-1])
        	del nums[-1]
        	k -= 1

if __name__ == '__main__':
	a = Solution()
	nums = []
	a.rotate(nums,2)
	print(nums)