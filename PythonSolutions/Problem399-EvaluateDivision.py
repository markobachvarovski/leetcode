from collections import defaultdict
from typing import List, Any


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):
        adj_list = defaultdict(list)
        answers = []

        for i, eqn in enumerate(equations):
            a, b = eqn
            adj_list[a].append([b, values[i]])
            adj_list[b].append([a, 1/values[i]])

        def search(start, target, weight):
            nonlocal visited

            if start == target:
                return weight

            visited.add(start)

            for vertex, w in adj_list[start]:
                if vertex not in visited:
                    found_weight = search(vertex, target, weight * w)
                    if found_weight != -1:
                        return found_weight
            return -1

        for query in queries:
            start, target = query

            if start not in adj_list or target not in adj_list:
                answers.append(-1)
            else:
                visited = set()
                answers.append(search(start, target, 1))

        return answers


if __name__ == '__main__':
    testCases = {
        1: [
            [["a","b"],["b","c"]],
            [2.0, 3.0],
            [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        ],
        2: [
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "a"]]
        ],
        3: [
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        ],
        4: [
            [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
            [3.0, 4.0, 5.0, 6.0],
            [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]
        ]
    }

    for key in testCases:
        print(Solution().calcEquation(testCases[key][0], testCases[key][1], testCases[key][2]))