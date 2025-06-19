from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        badIdx = -1  # Last index of invalid element
        minKIdx = -1  # Last index of minK
        maxKIdx = -1  # Last index of maxK

        for i in range(len(nums)):
            if not (minK <= nums[i] <= maxK):
                badIdx = i

            if nums[i] == minK:
                minKIdx = i
            if nums[i] == maxK:
                maxKIdx = i

            result += max(0, min(minKIdx, maxKIdx) - badIdx)

        return result


if __name__ == '__main__':
    testCases = {
        1: [[1,3,5,2,7,5], 1, 5],
        2: [[1,1,1,1], 1, 1]
    }

    for key in testCases:
        print(Solution().countSubarrays(testCases[key][0], testCases[key][1], testCases[key][2]))
