from collections import deque, defaultdict
from typing import Optional, List, Set
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, weight in times:
            graph[source].append((weight, target))

        # Distance from start_vertex to all other vertices
        weights = {vertex: float('inf') for vertex in range(1, n + 1)}
        weights[k] = 0
        min_heap = [(0, k)]

        while len(min_heap) > 0:
            curr_weight, curr_vertex = heapq.heappop(min_heap)

            # If the popped weight is greater than the existing weight for this vertex, skip
            if weights[curr_vertex] < curr_weight:
                continue

            for next_weight, next_vertex in graph[curr_vertex]:
                # Only go to next node, if its weight plus the current one is less than its existing weight
                if curr_weight + next_weight < weights[next_vertex]:
                    weights[next_vertex] = curr_weight + next_weight
                    heapq.heappush(min_heap, (weights[next_vertex], next_vertex))

        minTimeToTraverse = max(weights.values())
        if minTimeToTraverse == float('inf'):
            return -1
        return minTimeToTraverse

if __name__ == '__main__':
    testCases = {
        1: [[[2,1,1],[2,3,1],[3,4,1]], 4, 2],
        2: [[[1,2,1]], 2, 1],
        3: [[[1,2,1]], 2, 2]
    }

    for key in testCases:
        print(Solution().networkDelayTime(testCases[key][0], testCases[key][1], testCases[key][2]))