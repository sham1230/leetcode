class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set values for cheapest day and most profit
        # [7,1,5,3,6,4]
        # (-6, 4, -2, 3, -2)
        profit = 0
        # loop through list
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        
        return profit

        