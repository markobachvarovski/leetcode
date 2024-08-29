from collections import deque, defaultdict
from typing import Optional, List, Set
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for source, dest in tickets:
            graph[source].append(dest)
            graph[source] = sorted(graph[source])

        visited = set()
        source = 'JFK'
        finalAnswer = [source]
        while len(visited) < len(tickets):
            i = 0

            destination = graph[source][i]
            while (source, destination) in visited:
                destination = graph[source][i]
                i += 1

            if not graph[destination]:
                if len(visited) + 1 == len(tickets):
                    finalAnswer.append(destination)
                    return finalAnswer
                else:
                    continue

            visited.add((source, destination))
            finalAnswer.append(destination)
            source = destination

        return finalAnswer

if __name__ == '__main__':
    testCases = {
        1: [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],
        2: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
        3: [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]],
        4: [["JFK","AAA"],["AAA","JFK"],["JFK","BBB"],["JFK","CCC"],["CCC","JFK"]]
    }

    for key in testCases:
        print(Solution().findItinerary(testCases[key]))