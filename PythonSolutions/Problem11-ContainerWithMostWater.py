from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            maxArea = max(maxArea, (r - l) * min(height[l], height[r]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea

if __name__ == '__main__':
    testCases = {
        1: [1,8,6,2,5,4,8,3,7],
        2: [1,2,4,3]
    }

    for key in testCases:
        print(Solution().maxArea(testCases[key]))
