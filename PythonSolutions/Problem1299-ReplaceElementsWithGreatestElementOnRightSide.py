from typing import List
from collections import deque

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1] * len(arr)

        for i in range(len(arr) - 2, -1, -1):
            ans[i] = max(arr[i + 1], ans[i + 1])

        return ans




if __name__ == '__main__':
    testCases = {
        1: [17, 18, 5, 4, 6, 1],
        2: [400]
    }

    for key in testCases:
        print(Solution().replaceElements(testCases[key]))
