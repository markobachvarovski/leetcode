from collections import deque
from typing import Optional, List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(index: int, r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            if index == len(word) - 1:
                return True

            board[r][c] = '#'

            if dfs(index + 1, r - 1, c) \
                    or dfs(index + 1, r + 1, c) \
                    or dfs(index + 1, r, c - 1) \
                    or dfs(index + 1, r, c + 1):
                return True

            board[r][c] = word[index]
            return False



        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True

        return False

if __name__ == '__main__':
    testCases = {
        1: [
            [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ],
            "ABCCED"
        ],
    }

    for key in testCases:
        print(Solution().exist(testCases[key][0], testCases[key][1]))