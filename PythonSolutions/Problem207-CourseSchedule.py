from collections import deque, defaultdict
from typing import Optional, List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if course not in adj_list:
                return True

            visited.add(course)

            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            del adj_list[course]

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


if __name__ == '__main__':
    testCases = {
        1: [
          2,
          [[1,0]]
        ],
        2: [
          2,
          [[1,0],[0,1]]
        ],
        3: [
            20,
            [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
        ]
    }

    for key in testCases:
        print(Solution().canFinish(testCases[key][0], testCases[key][1]))