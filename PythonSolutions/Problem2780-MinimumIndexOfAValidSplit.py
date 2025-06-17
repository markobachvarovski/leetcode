from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxCountDominant = 0

        for element, count in freq.items():
            if count > maxCountDominant:
                dominantElement = element
                maxCountDominant = count

        dominantCount = 0
        for i in range(len(nums)):
            if nums[i] == dominantElement:
                dominantCount += 1

            # Check if split at position i is valid
            leftSize = i + 1
            rightSize = len(nums) - leftSize

            if (dominantCount > leftSize // 2 and
                    (maxCountDominant - dominantCount) > rightSize // 2):
                return i

        return -1


if __name__ == '__main__':
    testCases = {
        1: [1,2,2,2],
        2: [2,1,3,1,1,1,7,1,2,1]
    }

    for key in testCases:
        print(Solution().minimumIndex(testCases[key]))
