from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]

if __name__ == '__main__':
    testCases = {
        1: ["abcde", "abc"],
        2: ["abc", "abc"],
        3: ["abc", "def"]
    }

    for key in testCases:
        print(Solution().longestCommonSubsequence(testCases[key][0], testCases[key][1]))
