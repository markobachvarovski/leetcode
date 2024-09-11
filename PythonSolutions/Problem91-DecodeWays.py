class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':  # If string is empty or starts with 0, no valid decodings
            return 0

        n = len(s)
        dp = [0] * (n + 1)  # Create a dp array of size n+1
        dp[0] = 1  # There's 1 way to decode an empty string

        for i in range(1, n + 1):
            # Single digit decode (1-9)
            if s[i - 1] != '0':  # Check if single digit is valid (i.e., not '0')
                dp[i] += dp[i - 1]

            # Two digit decode (10-26)
            if i > 1 and '10' <= s[i - 2:i] <= '26':  # Check if two-digit number is valid
                dp[i] += dp[i - 2]

        return dp[n]

if __name__ == '__main__':
    testStrings = {
        1: "12",
        2: "226",
        3: "06"
    }

    for key in testStrings:
        print(Solution().numDecodings(testStrings[key]))
