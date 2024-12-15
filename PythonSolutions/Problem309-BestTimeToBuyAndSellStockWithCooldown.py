from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        # Initialize DP arrays
        dp_hold = [0] * n
        dp_sell = [0] * n
        dp_cooldown = [0] * n

        # Base cases
        dp_hold[0] = -prices[0]  # Buying the stock on day 0
        dp_sell[0] = 0  # Impossible to sell on day 0
        dp_cooldown[0] = 0  # No transaction yet

        # Fill DP arrays
        for i in range(1, n):
            # Either hold the stock from the previous day or buy a stock, in which case the profit is the profit of the cooldown state from before - the price
            dp_hold[i] = max(dp_hold[i - 1], dp_cooldown[i - 1] - prices[i])

            # If selling a stock, we get the profit from the holding state, plus the price of the stock
            dp_sell[i] = dp_hold[i - 1] + prices[i]

            # Either stay in cooldown (price of today = price of yesterday) or sell (for yesterday's price)
            dp_cooldown[i] = max(dp_cooldown[i - 1], dp_sell[i - 1])

        # The answer will be the maximum between being in cooldown or selling on the last day
        return max(dp_sell[-1], dp_cooldown[-1])


if __name__ == '__main__':
    testStrings = {
        1: [10,9,2,5,3,7,101,18],
        2: [0,1,0,3,2,3],
        3: [7,7,7,7,7,7,7]
    }

    for key in testStrings:
        print(Solution().lengthOfLIS(testStrings[key]))
