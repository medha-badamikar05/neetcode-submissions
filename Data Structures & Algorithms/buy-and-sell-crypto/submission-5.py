class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l,r = 0,0
        n = len(prices)
        while r < n:
            if prices[l] < prices[r]:
                # check difference
                sell = prices[r] - prices[l]
                maxProfit = max(sell, maxProfit)
            else:
                l = r
            r += 1
        return maxProfit
        