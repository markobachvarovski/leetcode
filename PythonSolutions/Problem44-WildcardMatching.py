
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # * can match empty string OR one more character
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # ? matches any single character, or exact match
                    dp[i][j] = dp[i - 1][j - 1]
                # else: dp[i][j] remains False (no match)

        return dp[m][n]


if __name__ == '__main__':
    testCases = {
        1: ["aa", "a"],
        2: ["aa", "*"],
        3: ["cb", "?a"],
        4: ["acbdebe", "a*be"]
    }

    for key in testCases:
        print(Solution().isMatch(testCases[key][0], testCases[key][1]))
