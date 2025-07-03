from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pair_map = defaultdict(int)
        count = 0

        for domino in dominoes:
            a, b = domino
            curr_pair = (min(a, b), max(a, b))
            count += pair_map[curr_pair]
            pair_map[curr_pair] += 1

        return count


if __name__ == '__main__':
    testCases = {
        1: [[1,2],[2,1],[3,4],[5,6]],
        2: [[1,2],[1,2],[1,1],[1,2],[2,2]]
    }

    for key in testCases:
        print(Solution().numEquivDominoPairs(testCases[key]))
