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
        i = 0;j = 0;inserted = 0
        while i < n:
            if j < m + inserted:
                if nums1[j] > nums2[i]:
                    nums1.insert(j,nums2[i])
                    i += 1
                    j += 1
                    inserted += 1
                    nums1.pop()
                else: j += 1
            else:
                nums1.insert(j,nums2[i])
                i += 1
                j += 1
                inserted += 1
                nums1.pop()
#test                
if __name__ == '__main__':    
    a = Solution()
    nums1 = []
    nums2 = []
    m = 0;n = 0
    a.merge(nums1,m,nums2,n)
