# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:16:43 2018

@author: shuli
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:return
        i = 0
        if nums2[0] <= nums1[0]:
                nums1.insert(0,nums2[0])
        while i < n:
            if nums2[i] >= nums1[m+i-1]:
                for s in nums2[i:]:
                    nums1.insert(m+i,s)
                    i += 1
                break
            left = 0;right = m+i-1;flag = True
            while left < right:
                mid = (left + right) // 2
                if nums2[i] == nums1[mid]:
                    nums1.insert(mid,nums2[i])
                    flag = False
                    break
                elif nums2[i] > nums1[mid]:
                    left = mid + 1
                else: right = mid - 1
            if flag:
                nums1.insert(left,nums2[i]) if nums1[left] > nums2[i] else nums1.insert(left+1,nums2[i])
            i += 1
        return 
if __name__ == '__main__':
    a = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3;n = 3
    a.merge(nums1,m,nums2,n)
