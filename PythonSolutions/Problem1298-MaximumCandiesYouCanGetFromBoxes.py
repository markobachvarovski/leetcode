from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        availableBoxes = set(initialBoxes)
        haveKeys = set()
        visited = set()
        totalCandies = 0

        queue = deque()

        # Enqueue boxes that are either open or we have keys for
        for box in initialBoxes:
            if status[box] == 1 or box in haveKeys:
                queue.append(box)

        while queue:
            box = queue.popleft()

            # Skip box if already processed
            if box in visited:
                continue

            visited.add(box)
            totalCandies += candies[box]

            # Collect keys and enqueue owned boxes that the new keys might open
            for key in keys[box]:
                haveKeys.add(key)
                if key in availableBoxes and key not in visited:
                    queue.append(key)

            # Collect boxes and enqueue them if we've found a key previously or they're opened by default
            for newBox in containedBoxes[box]:
                availableBoxes.add(newBox)
                if (status[newBox] == 1 or newBox in haveKeys) and newBox not in visited:
                    queue.append(newBox)

        return totalCandies




if __name__ == '__main__':
    testCases = {
        1: [[1,0,1,0],
            [7,5,4,100],
            [[],[],[1],[]],
            [[1,2],[3],[],[]],
            [0]],
        2: [[1,0,0,0,0,0],
            [1,1,1,1,1,1],
            [[1,2,3,4,5],[],[],[],[],[]],
            [[1,2,3,4,5],[],[],[],[],[]],
            [0]]
    }

    for key in testCases:
        print(Solution().maxCandies(testCases[key][0], testCases[key][1], testCases[key][2], testCases[key][3], testCases[key][4]))
