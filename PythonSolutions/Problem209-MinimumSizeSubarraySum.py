from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target: return 0  # <-- 1

        s, l, ans = 0, 0, len(nums) + 1  # <-- 2

        for r, val in enumerate(nums):  #
            s += val  #
            while s >= target:  # <-- 3
                s -= nums[l]  #
                ans = min(ans, r - l + 1)  #
                l += 1  #

        if ans == len(nums) + 1:
            ans = 0
        return ans


if __name__ == '__main__':
    testNums = {
        1: [7, [2,3,1,2,4,3]],
        2: [4, [1,4,4]],
        3: [11, [1,9,1,1,1,1,1,8,3,1]],
    }

    for key in testNums:
        print(Solution().minSubArrayLen(testNums[key][0], testNums[key][1]))