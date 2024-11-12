import heapq
from typing import List
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            x, y = point
            heapq.heappush(max_heap, (-math.sqrt(x ** 2 + y ** 2), point))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [element[1] for element in max_heap]


if __name__ == '__main__':
    testCases = {
        1: [[[3,3],[5,-1],[-2,4]], 2],
        2: [[[1,3],[-2,2]], 1]
    }

    for key in testCases:
        print(f"{Solution().kClosest(testCases[key][0], testCases[key][1])}")
