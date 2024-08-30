from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()
        solutions = 0

        def backtrack(r):
            nonlocal solutions
            if r == n:
                solutions += 1
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return solutions


if __name__ == '__main__':
    testCases = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5
    }

    for key in testCases:
        print(f"{Solution().totalNQueens(testCases[key])}")
