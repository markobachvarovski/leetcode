from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

if __name__ == '__main__':
    testStrings = {
        1: [10,9,2,5,3,7,101,18],
        2: [0,1,0,3,2,3],
        3: [7,7,7,7,7,7,7]
    }

    for key in testStrings:
        print(Solution().lengthOfLIS(testStrings[key]))
