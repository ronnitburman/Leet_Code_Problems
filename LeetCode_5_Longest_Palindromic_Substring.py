class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sr=''
        len_max = 0
        for i in range(len(s)):
            #odd
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len_max < (r-l+1):
                    sr=s[l:r+1]
                    len_max= r-l+1
                l-=1
                r+=1
                    
            #even
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len_max < (r-l+1):
                    sr=s[l:r+1]
                    len_max= r-l+1
                l-=1
                r+=1
        return sr