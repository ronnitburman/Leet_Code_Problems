class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # if len(arr)>1:
        #     for i in range(len(arr)-1):
        #         arr[i]=max(arr[(i+1):])
        #     arr[len(arr)-1]= -1
        #     return arr
        # else:
        #     return[-1]

        if len(arr)>1:
            maxm = -1
            for i in range(len(arr)):
                temp = arr[len(arr)-i-1]
                arr[len(arr)-i-1] = maxm
                maxm = max(maxm, temp)
            return arr
        else:
            return [-1]