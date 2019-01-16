#url https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#writtenby:anhty9le

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        i=0
        n=len(prices)
        prices.append(0)
        prices.append(0)
        buy=0
        sell=0
        while buy<n-1 and sell<n-1:
            while prices[buy]>=prices[buy+1] and buy<n-1:
                buy+=1
                
            sell=buy+1
            while prices[sell]<=prices[sell+1] and sell<n-1:
                sell+=1
                
            if prices[sell]-prices[buy]>0:
                profit+=prices[sell]-prices[buy]
                
            buy=sell+1
            
        return(profit)
        