class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, b = prices[0], 0
        for p in prices[1:]:
            b = max(b, p - l)
            l = min(l, p)
        return b
