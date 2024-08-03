from collections import deque
from typing import Optional, List, Set


class Solution:
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        visitedPacific, visitedAtlantic, atlanticFlow, pacificFlow = set(), set(), set(), set()
        q = deque()
        answer = []
        def bfs(r, c, prevR, prevC, visited, flow):
            if (
                r < 0
                or c < 0
                or r == rows
                or c == cols
                or heights[r][c] < heights[prevR][prevC]
            ):
                return

            if (r, c) in visited:
                return
            visited.add((r, c))
            flow.add((r, c))
            q.append([r, c])

        for c in range(cols):
            atlanticFlow.add((rows-1, c))
            q.append((rows - 1, c))
        for r in range(rows):
            atlanticFlow.add((r, cols - 1))
            q.append((r, cols - 1))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r + 1, c, r, c, visitedAtlantic, atlanticFlow)
                bfs(r - 1, c, r, c, visitedAtlantic, atlanticFlow)
                bfs(r, c + 1, r, c, visitedAtlantic, atlanticFlow)
                bfs(r, c - 1, r, c, visitedAtlantic, atlanticFlow)

        for c in range(cols):
            pacificFlow.add((0, c))
            q.append((0, c))
        for r in range(rows):
            pacificFlow.add((r, 0))
            q.append((r, 0))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r + 1, c, r, c, visitedPacific, pacificFlow)
                bfs(r - 1, c, r, c, visitedPacific, pacificFlow)
                bfs(r, c + 1, r, c, visitedPacific, pacificFlow)
                bfs(r, c - 1, r, c, visitedPacific, pacificFlow)

        for pair in atlanticFlow:
            if pair in pacificFlow:
                r,c = pair
                answer.append([r, c])

        return answer


if __name__ == '__main__':
    testCases = {
        1: [
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]
        ],
        2: [[1]]
    }

    for key in testCases:
        print(Solution().pacificAtlantic(testCases[key]))