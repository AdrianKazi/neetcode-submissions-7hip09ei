class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force O(n2)
        # max_profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         max_profit = max(prices[j] - prices[i], max_profit)

        # return max_profit

        # Dynamic Programming O(n)
        maxProfit = 0
        minBuy = prices[0]

        for sell in prices:
            maxProfit = max(maxProfit, sell - minBuy)
            minBuy = min(minBuy, sell)

        return maxProfit