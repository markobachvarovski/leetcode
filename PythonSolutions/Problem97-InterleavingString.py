from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(1, len(s1) + 1):
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True

        for j in range(1, len(s2) + 1):
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
                dp[0][j] = True

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                if dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True

        return dp[-1][-1]

if __name__ == '__main__':
    testStrings = {
        1: ["aabcc", "dbbca", "aadbbcbcac"],
        2: ["aabcc", "dbbca", "aadbbbaccc"],
    }

    for key in testStrings:
        print(Solution().isInterleave(testStrings[key][0], testStrings[key][1], testStrings[key][2]))
