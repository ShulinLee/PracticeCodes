class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - k
        nums[:] = nums[n:] + nums[:n]

if __name__ == '__main__':
	a = Solution()
	nums = [1,2,3,4,5,6,7]
	a.rotate(nums,3)
	print(nums)