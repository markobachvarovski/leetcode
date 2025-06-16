from os import times
from typing import List
from collections import defaultdict, deque
from heapq import heappush, heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))


        times = [float('inf')] * n
        num_ways = [0] * n

        times[0] = 0
        num_ways[0] = 1

        queue = []
        queue.append((0, 0))

        while queue:
            path, time = heappop(queue)

            if time > times[path]:
                continue

            for next_path, next_time in graph[path]:
                time_to_neighbor = time + next_time

                if time_to_neighbor < times[next_path]:
                    num_ways[next_path] = num_ways[path]
                    times[next_path] = time_to_neighbor

                    heappush(queue, (next_path, time_to_neighbor))
                elif time_to_neighbor == times[next_path]:
                    num_ways[next_path] = (num_ways[next_path] + num_ways[path]) % (10**9 + 7)

        return num_ways[-1]



if __name__ == '__main__':
    testCases = {
        1: [7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]],
        2: [2, [[1,0,10]]]
    }

    for key in testCases:
        print(Solution().countPaths(testCases[key][0], testCases[key][1]))
