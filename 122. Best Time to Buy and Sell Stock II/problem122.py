# These imports are to avoid errors if ran in an IDE
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0

        # Greedy solution: if there is a profit, immediately take it
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profits += prices[i+1] - prices[i]

        return profits
