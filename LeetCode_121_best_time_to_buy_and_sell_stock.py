class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        l=0
        maxm=0
        for r in range(len(prices)):
            if prices[r]<prices[l]:
                l=r
            else:
                maxm=max(maxm, prices[r]-prices[l])
                
        return maxm