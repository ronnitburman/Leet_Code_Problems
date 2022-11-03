class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm={}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in hm:
                return i,hm[diff]
            hm[n]=i