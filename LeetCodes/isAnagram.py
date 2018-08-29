class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
        	return False
        return self.countDict(s) == self.countDict(t)

    def countDict(self,str):
    	dic = {}
    	for ch in str:
    		dic[ch] = dic.get(ch,0)
    		dic[ch] += 1
    	return dic