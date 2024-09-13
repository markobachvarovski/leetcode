from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]

if __name__ == '__main__':
    testStrings = {
        1: [[1, 2, 5], 11],
        2: [[2], 3],
        3: [[1], 0],
        4: [[186,419,83,408], 6249]
    }

    for key in testStrings:
        print(Solution().coinChange(testStrings[key][0], testStrings[key][1]))
