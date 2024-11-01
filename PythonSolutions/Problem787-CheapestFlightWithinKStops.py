from collections import deque, defaultdict
from typing import Optional, List, Set
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = [[] for _ in range(n)]
        for source, dest, price in flights:
            edges[source].append((dest, price))

        heap = [(0, src, 0)]
        maxStops = {}
        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > k or (node in maxStops and maxStops[node] <= stops):
                continue
            maxStops[node] = stops

            for dest, price in edges[node]:
                heapq.heappush(heap, (price + cost, dest, stops + 1))
        return -1

if __name__ == '__main__':
    testCases = {
        1: [
            4,
            [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
            0,
            3,
            1
        ],
        2: [
            3,
            [[0,1,100],[1,2,100],[0,2,500]],
            0,
            2,
            1
        ],
        3: [
            3,
            [[0,1,100],[1,2,100],[0,2,500]],
            0,
            2,
            0
        ],
        4: [
            10,
            [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],
            6,
            0,
            7
        ],
        5: [
            4,
            [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
            0,
            3,
            1
        ]
    }

    for key in testCases:
        print(Solution().findCheapestPrice(testCases[key][0], testCases[key][1], testCases[key][2], testCases[key][3], testCases[key][4]))