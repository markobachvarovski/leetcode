from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif j - 1 < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]

if __name__ == '__main__':
    testCases = {
        1: [6, 3],
        2: [12, 12]
    }

    for key in testCases:
        print(Solution().uniquePaths(testCases[key][0], testCases[key][1]))
