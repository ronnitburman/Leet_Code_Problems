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
        #in case we have to solve without using a string
        # if x<0: 
        #     return False
        # div=1
        
        # while x>=10*div :
        #     div*=10
        
        # while x:
        #     if x//div != x%10: return False
        #     x = (x%div)//10
        #     div/=100
        # return True