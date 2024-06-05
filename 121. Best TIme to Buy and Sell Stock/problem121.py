# These imports are to avoid errors if ran in an IDE
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This is a greedy algorithm that consistently grabs the smallest price as the buy price
        and calculates the profit based on the current buy price
        """
        buy_price = prices[0]
        profit = 0

        for price in prices:
            if buy_price > price:
                buy_price = price

            profit = max(profit, price - buy_price)

        return profit
