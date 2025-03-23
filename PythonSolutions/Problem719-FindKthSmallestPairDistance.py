from typing import List
from heapq import heappush, heappop

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = abs(nums[i] - nums[j])
                if len(max_heap) < k:
                    heappush(max_heap, -diff)
                    continue
                if len(max_heap) >= k and -max_heap[0] > diff:
                    heappop(max_heap)
                    heappush(max_heap, -diff)

        return -max_heap[0]


if __name__ == '__main__':
    testCases = {
        1: [10,15,20],
        2: [1,100,1,1,1,100,1,1,100,1]
    }

    for key in testCases:
        print(f"{Solution().minCostClimbingStairs(testCases[key])}")
