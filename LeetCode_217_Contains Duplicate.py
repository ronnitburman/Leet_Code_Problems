class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #since a set has only unique elements -> if length of set(nums) is less than nums then nums has to have dublicates
        return len(set(nums))!=len(nums)