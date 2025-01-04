from collections import deque, defaultdict
from typing import Optional, List, Set
import heapq


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        adj_list = defaultdict(list)
        for src, dest, count in edges:
            adj_list[src].append((dest, count))
            adj_list[dest].append((src, count))

        heap = [(-maxMoves, 0)]
        visited = {}
        answer = 0

        reachable_subdivisions = defaultdict(int)

        while heap:
            remaining_moves, node = heapq.heappop(heap)
            remaining_moves = -remaining_moves

            if node in visited and visited[node] >= remaining_moves:
                continue
            visited[node] = remaining_moves

            answer += 1

            for neighbor, edge_count in adj_list[node]:
                # Check how many nodes along this edge we can reach
                reachable_along_edge = min(edge_count, remaining_moves)
                reachable_subdivisions[(node, neighbor)] = max(reachable_subdivisions[(node, neighbor)],
                                                               reachable_along_edge)

                # If we have enough moves to reach the neighbor node itself
                if remaining_moves > edge_count and (
                        neighbor not in visited or visited[neighbor] < remaining_moves - edge_count - 1):
                    heapq.heappush(heap, (-(remaining_moves - edge_count - 1), neighbor))

        # Count all reachable subdivisions between nodes
        for u, v, count in edges:
            answer += min(count, reachable_subdivisions[(u, v)] + reachable_subdivisions[(v, u)])

        return answer


if __name__ == '__main__':
    testCases = {
        1: [[1,2,2],[3,8,2],[5,3,5]],
        2: [[1,2,3],[3,8,4],[5,3,5]],
        3: [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
        4: [[1,10,6,7,9,10,4,9]]
    }

    for key in testCases:
        print(Solution().minimumEffortPath(testCases[key]))