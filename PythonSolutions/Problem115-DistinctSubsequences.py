from typing import List


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1


        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]

if __name__ == '__main__':
    testStrings = {
        1: ["rabbbit", "rabbit", ],
        2: ["babgbag", "bag"],
    }

    for key in testStrings:
        print(Solution().numDistinct(testStrings[key][0], testStrings[key][1]))
