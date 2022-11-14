class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[[1]]
        for i in range(1,numRows):
            res.append([0,*res[i-1]])
            temp = res[i]+[0]
            for j in range(len(temp)-1):
                res[i][j]=temp[j]+temp[j+1]
        return res