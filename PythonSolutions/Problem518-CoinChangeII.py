from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]

        return dp[amount]



if __name__ == '__main__':
    testStrings = {
        1: [[1, 2, 5], 5],
        2: [[2], 3],
        3: [[1], 0],
        4: [[186,419,83,408], 6249]
    }

    for key in testStrings:
        print(Solution().coinChange(testStrings[key][0], testStrings[key][1]))
