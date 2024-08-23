# Definition for a Node.
from collections import defaultdict
from typing import Optional, List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        answer = []
        def dfs(r, c, currWord):
            nonlocal answer

            if r < 0 or c < 0 or r >= rows or col >= cols or (r, c) in visited:
                return

            if currWord in words and currWord not in answer:
                answer.append(currWord)
                return

            currWord += board[r][c]
            visited.add((r,c))

            dfs(r + 1, c, currWord)
            dfs(r - 1, c, currWord)
            dfs(r, c + 1, currWord)
            dfs(r, c - 1, currWord)

        for row in range(rows):
            for col in range(cols):
                visited = set()
                dfs(row, col, '')

        return answer

if __name__ == '__main__':
    testCases = {
        1: [
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"]
            ],
            ["oath", "pea", "eat", "rain"]
        ],
    }

    for key in testCases:
        print(Solution().findWords(testCases[key][0], testCases[key][1]))