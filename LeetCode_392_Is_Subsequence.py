class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)<1:
            return False
        else:
            flag = True
            countr = 0
            for sub in s:
                if sub in t:
                    if countr<=t.index(sub):
                        countr =t.index(sub)
                    else:
                        flag=False
                else:
                    flag=False

            return flag