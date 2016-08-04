class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices: return 0
        low, maxProfit = prices[0], 0
        
        for p in prices:
            maxProfit = max(maxProfit, p - low)
            low = min(low, p)
        
        return maxProfit