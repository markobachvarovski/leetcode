from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > maxProfit:
                maxProfit = price - minPrice

        return maxProfit

if __name__ == '__main__':
    testCases = {
        1: [7,1,5,3,6,4],
        2: [7,6,4,3,1],
    }

    for key in testCases:
        print(Solution().maxProfit(testCases[key]))

