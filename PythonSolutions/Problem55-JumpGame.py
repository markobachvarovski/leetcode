from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        localMaxJump = nums[0]
        currIndex = 0

        while localMaxJump > 0:
            if currIndex >= len(nums) - 1:
                return True

            localMaxJump = 0
            for i in range(currIndex, currIndex + nums[currIndex]):
                if nums[i] >= localMaxJump:
                    localMaxJump = nums[i]

            currIndex = currIndex + localMaxJump

        return False


if __name__ == '__main__':
    testCases = {
        1: [2,3,1,1,4],
        2: [3,2,1,0,4]
    }

    for key in testCases:
        print(Solution().canJump(testCases[key]))
