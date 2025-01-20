from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        numFlipped = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                numFlipped += 1
            if numFlipped > k:
                if nums[l] == 0:
                    numFlipped -= 1
                l += 1

        return r - l + 1


if __name__ == '__main__':
    testCases = {
        1: [[1,1,1,0,0,0,1,1,1,1,0], 2],
        2: [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3]
    }

    for key in testCases:
        print(Solution().longestOnes(testCases[key][0], testCases[key][1]))