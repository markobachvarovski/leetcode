from collections import deque
from typing import Optional, List, Set
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        map = {}

        for i in nums:
            if i not in map.keys():
                map[i] = 1
            else:
                map[i] += 1

        for num in map.keys():
            heapq.heappush(min_heap, (map[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap]


if __name__ == '__main__':
    testCases = {
        1: [[1,1,1,2,2,3], 2],
        2: [[1], 1],
    }

    for key in testCases:
        print(Solution().topKFrequent(testCases[key][0], testCases[key][1]))