class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        hashmap = set()
        l=0
        for r in range(len(s)):
            while s[r] in hashmap:
                hashmap.remove(s[l])
                l+=1
            hashmap.add(s[r])    
            count = max(count, r-l+1)
        return count