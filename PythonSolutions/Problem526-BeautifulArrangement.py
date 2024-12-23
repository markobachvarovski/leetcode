from bisect import bisect
from random import randint
from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1)

        def findBeautiful(i):
            if i == n + 1:
                return 1
            count = 0
            for num in range(1, n + 1):
                if (not visited[num]) and (i % num == 0 or num % i == 0):
                    visited[num] = True
                    count += findBeautiful(i + 1)
                    visited[num] = False
            return count

        return findBeautiful(1)

if __name__ == '__main__':
    testCases = {
        1: 1,
        2: 2,
        3: 3,
        4: 4
    }

    for key in testCases:
        print(Solution().countArrangement(testCases[key]))
