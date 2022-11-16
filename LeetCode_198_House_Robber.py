class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Base cases:

        1) If we only have one house to rob, we rob it
        2) If we have only two houses to rob, then we cannot rob both so we rob the one with the most money
        
        That was pretty simple! But what if we have more than two houses? Well, let's think about it as 
        if we are at the nth house and we already robbed the previous houses. We can either rob this 
        house or not. If we do rob the house, we cannot rob the n-1th house, so the total amount of 
        money we get is the total amount of money after robbing the first n-2 houses plus the money at
        the nth house. If we don't rob the nth house, then we still have the same amount of money as we 
        had after robbing the n-1th house. 
        Using this, we can construct our first solution:
        """
        if len(nums)==1:
            return nums[0]
        if len (nums) == 2:
            return max(nums[0],nums[1])
        
        prev2=nums[0]
        prev=nums[1]
        for i in range(2,len(nums)):
            curr = nums[i]+prev2
            if curr>prev:
                prev2=max(prev2,prev)
                prev=curr
            else:
                temp = prev2
                prev2=prev
                prev=temp
        return max(prev, prev2)
            
            