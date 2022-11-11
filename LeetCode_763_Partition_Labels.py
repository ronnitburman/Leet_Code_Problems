class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        result=[]
        hashmap = {}
        count = 0
        max_idx = 0
        
        for i,char in enumerate(s):
            hashmap[char]=i
        for i,char in enumerate(s):
            max_idx = max(max_idx, hashmap[char])
            count+=1
            if i==max_idx:
                result.append(count)
                count=0
        return result