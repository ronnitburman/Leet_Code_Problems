class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strn=''
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if len(strs[j])<=i or strs[j][i]!=strs[0][i]:
                    return strn
            strn = strn+strs[0][i]
        return strn