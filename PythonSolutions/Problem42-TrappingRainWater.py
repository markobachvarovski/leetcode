from typing import List

class Solution:

    def trap(self, height: List[int]) -> int:
        l = 0
        leftMax = height[l]

        r = len(height) - 1
        rightMax = height[r]

        waterTrapped = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                waterTrapped += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                waterTrapped += rightMax - height[r]

        return waterTrapped

if __name__ == '__main__':
    testCases = {
        1: [0,1,0,2,1,0,1,3,2,1,2,1],
        2: [4,2,0,3,2,5]
    }

    for key in testCases:
        print(Solution().trap(testCases[key]))
