from collections import deque
from typing import Optional, List, Set
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def get_cost(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        mst = []
        visited = set()

        # Min-heap to pick the smallest edge
        min_heap = [(0, 0, 0)]
        total_weight = 0

        while len(mst) < len(points) - 1:
            weight, from_point, to_point = heapq.heappop(min_heap)
            if to_point in visited:
                continue

            visited.add(to_point)
            total_weight += weight
            if from_point != to_point:
                mst.append((from_point, to_point, weight))

            for next_point in range(len(points)):
                if next_point not in visited:
                    distance = get_cost(points[to_point][0], points[to_point][1], points[next_point][0], points[next_point][1])
                    heapq.heappush(min_heap, (distance, to_point, next_point))

        return total_weight

if __name__ == '__main__':
    testCases = {
        1: [[0,0],[2,2],[3,10],[5,2],[7,0]],
        2: [[3,12],[-2,5],[-4,1]],
    }

    for key in testCases:
        print(Solution().minCostConnectPoints(testCases[key]))