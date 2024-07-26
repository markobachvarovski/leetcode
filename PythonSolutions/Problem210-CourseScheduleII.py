from collections import deque, defaultdict
from typing import Optional, List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        visited = set()
        answer = []
        def dfs(course):
            nonlocal answer
            if course in cycle:
                return False

            if course in visited:
                return True

            # if course not in adj_list:
            #     answer.append(course)
            #     visited.add(course)
            #     return

            # visited.add(course)
            cycle.add(course)

            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)
            answer.append(course)
            return True

        for course in range(numCourses):
            cycle = set()
            if not dfs(course):
                return []

        return answer


if __name__ == '__main__':
    testCases = {
        1: [
          2,
          [[1,0]]
        ],
        2: [
          4,
          [[1,0],[2,0],[3,1],[3,2]]
        ],
        3: [
            1,
            []
        ],
        4: [
            3,
            [[1, 0], [0, 2], [2, 1]]
        ],
        5: [
            7,
            [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]
        ]
    }

    for key in testCases:
        print(Solution().canFinish(testCases[key][0], testCases[key][1]))