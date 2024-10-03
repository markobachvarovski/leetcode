from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad the nums array with 1 at both ends
        nums = [1] + nums + [1]
        n = len(nums)

        # Initialize a DP table with 0s
        dp = [[0] * n for _ in range(n)]

        # Iterate through all possible lengths of subarrays
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length

                for i in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right]
                    )

        return dp[0][-1]

if __name__ == '__main__':
    testStrings = {
        1: [[1,1,1,1,1], 3],
        2: [[1], 1],
    }

    for key in testStrings:
        print(Solution().maxCoins(testStrings[key][0], testStrings[key][1]))
