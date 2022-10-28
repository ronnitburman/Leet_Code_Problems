class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x) #converting to a string since its easier to access the elements
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True