# 121. Best Time to Buy and Sell Stock  QuestionEditorial Solution

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        max_profit = 0
        min_price = prices[0]
        for p in prices:
            if min_price > p: min_price = p
            if max_profit < (p-min_price): max_profit = p-min_price
        return max_profit
