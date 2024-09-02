from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        oneStep, twoSteps = 1, 1
        for i in range(n-1):
            temp = oneStep
            oneStep += twoSteps
            twoSteps = temp

        return oneStep

if __name__ == '__main__':
    testCases = {
        1: 2,
        2: 3,
        3: 5
    }

    for key in testCases:
        print(f"{Solution().climbStairs(testCases[key])}")
