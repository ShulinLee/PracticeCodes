# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 10:51:57 2018

@author: shuli
"""

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #找最短的字符串作为插入字符串
        if len(l1) < len(l2):
            insert = l1
            inserted = l2
        else:
            insert = l2
            inserted = l1
        start = 0
        
        for num in insert:  
            if num >= inserted[-1]:
                inserted.insert(len(inserted),num)
            elif num <= inserted[start]:
                inserted.insert(start,num)
                start = inserted.index(num)
            else:
                for i in range(start,len(inserted)):
                    if num >= inserted[i] and num <= inserted[i+1]:
                        inserted.insert(i+1,num)
                        break
                start = inserted.index(num)
                
        return inserted

if __name__ == '__main__':
    a = Solution()
    l1 = [1,5,8,11]
    l2 = [2,3]
    print(a.mergeTwoLists(l1,l2))
                    