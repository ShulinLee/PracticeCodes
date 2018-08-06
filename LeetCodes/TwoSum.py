class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in nums:
                j = nums.index(diff)
                if i!= j:
                    return [i,j]
            else:
                continue
