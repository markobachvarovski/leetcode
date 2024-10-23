from collections import deque, defaultdict
from typing import Optional, List, Set
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        adj_list = defaultdict(list)
        for i, edge in enumerate(edges):
            src, dest = edge
            adj_list[src].append((succProb[i], dest))
            adj_list[dest].append((succProb[i], src))

        weights = {vertex: float('-inf') for vertex in range(0, n + 1)}
        weights[start_node] = 1
        max_heap = [(-1, start_node)]
        visited = set()

        while len(max_heap) > 0:
            prob, node = heapq.heappop(max_heap)
            prob *= -1

            if node in visited:
                continue
            visited.add(node)

            for next_prob, next_node in adj_list[node]:
                if prob * next_prob > weights[next_node]:
                    weights[next_node] = prob * next_prob
                    heapq.heappush(max_heap, (-weights[next_node], next_node))

        if weights[end_node] == float('-inf'):
            return 0

        return weights[end_node]

if __name__ == '__main__':
    testCases = {
        1: [3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2],
        2: [3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2],
        3: [3, [[0,1]], [0.5], 0, 2],
    }

    for key in testCases:
        print(Solution().maxProbability(testCases[key][0], testCases[key][1], testCases[key][2], testCases[key][3], testCases[key][4]))