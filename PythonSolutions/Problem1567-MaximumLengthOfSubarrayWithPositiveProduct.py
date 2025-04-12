from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        subarrays = []
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == 0:
                subarrays.append(nums[left:right])
                left = right + 1
            right += 1
        subarrays.append(nums[left:right])

        globalMax = 0
        for subarray in subarrays:
            productLength = 0
            countNegatives = 0
            firstNegative = -1
            lastNegative = -1
            for i, num in enumerate(subarray):
                if num < 0:
                    countNegatives += 1
                    lastNegative = i
                    if firstNegative == -1:
                        firstNegative = i

            if countNegatives % 2 == 0:
                globalMax = max(globalMax, len(subarray))
            else:
                globalMax = max(globalMax, len(subarray) - 1 - firstNegative, lastNegative)
        return globalMax


if __name__ == '__main__':
    testCases = {
        1: [1,-2,-3,4],
        2: [0,1,-2,-3,-4],
        3: [-1,-2,-3,0,1]
    }

    for key in testCases:
        print(Solution().getMaxLen(testCases[key]))
