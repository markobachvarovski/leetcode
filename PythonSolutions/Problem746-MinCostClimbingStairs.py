from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])


if __name__ == '__main__':
    testCases = {
        1: [10,15,20],
        2: [1,100,1,1,1,100,1,1,100,1]
    }

    for key in testCases:
        print(f"{Solution().minCostClimbingStairs(testCases[key])}")
