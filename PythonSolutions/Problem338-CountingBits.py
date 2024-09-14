from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i // 2] + (i % 2)

        return dp

if __name__ == '__main__':
    testStrings = {
        1: 2,
        2: 5,
        3: 6,
        4: 10
    }

    for key in testStrings:
        print(Solution().countBits(testStrings[key]))
