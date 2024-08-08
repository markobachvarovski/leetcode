from collections import deque, defaultdict
from typing import Optional, List, Set


class UnionFind:

    def __init__(self):
        self.f = {}

    def findParent(self, x: int) -> int:
        y = self.f.get(x, x)
        if x != y:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x: int, y: int):
        self.f[self.findParent(x)] = self.findParent(y)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a, b in edges:
            dsu.union(a, b)
        return len(set(dsu.findParent(x) for x in range(n)))

if __name__ == '__main__':
    testCases = {
        1: [3, [[0,1], [0,2]]],
        2: [6, [[0,1], [1,2], [2,3], [4,5]]]
    }

    for key in testCases:
        print(Solution().countComponents(testCases[key][0], testCases[key][1]))