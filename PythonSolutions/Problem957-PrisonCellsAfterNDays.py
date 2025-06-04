from typing import List
from collections import deque

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        if n == 0:
            return cells

        def nextDay(state):
            result = [0] * 8
            for i in range(1, 7):
                if state[i - 1] == state[i + 1]:
                    result[i] = 1
            return result

        seen = {}
        current = cells[:]

        for day in range(n):
            key = tuple(current)
            if key in seen:
                # Found cycle
                cycle_length = day - seen[key]
                remaining = (n - day) % cycle_length
                for _ in range(remaining):
                    current = nextDay(current)
                return current

            seen[key] = day
            current = nextDay(current)

        return current


if __name__ == '__main__':
    testCases = {
        1: [[0,1,0,1,1,0,0,1], 7],
        2: [[1,0,0,1,0,0,1,0], 1000000000]
    }

    for key in testCases:
        print(Solution().prisonAfterNDays(testCases[key][0], testCases[key][1]))
