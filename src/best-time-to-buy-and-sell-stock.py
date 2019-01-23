# url https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# writtenby:anhty9le


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        while len(prices) > 1 and prices[0] > prices[1]:
            prices.pop(0)

        profit = 0
        price = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                price = prices[j] - prices[i]
                if profit < price:
                    profit = price

        return (profit)
