from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows, cols = len(board), len(board[0])

        q = deque()
        q.append([1, 0])
        visited = set()
        max_field = rows * cols

        while q:
            curr, count = q.popleft()

            for i in range(1, 7):
                next = curr + i
                curr_row = rows - 1 - ((next - 1) // rows)
                curr_col = (next - 1) % cols
                if (rows - 1 - curr_row) % 2 == 1:
                    curr_col = cols - 1 - curr_col

                if board[curr_row][curr_col] != -1:
                    next = board[curr_row][curr_col]

                if next == max_field:
                    return count + 1

                if next not in visited:
                    q.append([next, count + 1])
                    visited.add(next)

        return -1

if __name__ == '__main__':
    testNums = {
        1: [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,35,-1,-1,13,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,15,-1,-1,-1,-1]
        ],
        2: [
            [-1, -1, 19, 10, -1],
            [2, -1, -1, 6, -1],
            [-1, 17, -1, 19, -1],
            [25, -1, 20, -1, -1],
            [-1, -1, -1, -1, 15]
        ]
    }

    for key in testNums:
        print(Solution().snakesAndLadders(testNums[key]))