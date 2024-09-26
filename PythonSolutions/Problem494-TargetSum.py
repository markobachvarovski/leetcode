from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        newTarget = target + sum(nums)

        if newTarget % 2 == 1:
            return 0

        newTarget = newTarget // 2

        dp = [0] * (newTarget + 1)
        dp[0] = 1

        for num in nums:
            for j in range(newTarget, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[newTarget]



if __name__ == '__main__':
    testStrings = {
        1: [[1,1,1,1,1], 3],
        2: [[1], 1],
    }

    for key in testStrings:
        print(Solution().findTargetSumWays(testStrings[key][0], testStrings[key][1]))
