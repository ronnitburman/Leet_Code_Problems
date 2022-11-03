class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_s={}
        hash_t={}
        if len(s)==len(t):
            for i in range(len(s)):
                hash_s[s[i]] = hash_s.get(s[i],0)+ 1
                hash_t[t[i]] = hash_t.get(t[i],0)+ 1
                
            return hash_s == hash_t
        else:
            return False