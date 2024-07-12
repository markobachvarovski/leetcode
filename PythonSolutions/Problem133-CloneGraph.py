from collections import deque
from typing import Optional, List, Set

class GraphNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Optional[GraphNode]) -> Optional[GraphNode]:
        if not node:
            return

        newNodes = {}
        def dfs(node: Optional[GraphNode]):
            nonlocal newNodes

            if node in newNodes:
                return node

            newNode = GraphNode(node.val)
            newNodes[node] = newNode

            for neighbour in node.neighbors:
                newNode.neighbors.append(dfs(neighbour))

        def bfs(node: Optional[GraphNode]):
            nonlocal newNodes
            queue = deque()
            queue.append(node)

            while queue:
                node = queue.popleft()

                if node not in newNodes:
                    newNode = GraphNode(node.val)
                    newNodes[node] = newNode
                else:
                    if newNodes[node].neighbors:
                        continue
                    newNode = newNodes[node]

                for neighbor in node.neighbors:
                    if neighbor not in newNodes:
                        newNeighbor = GraphNode(neighbor.val)
                        newNodes[neighbor] = newNeighbor
                    else:
                        newNeighbor = newNodes[neighbor]

                    newNode.neighbors.append(newNeighbor)
                    queue.append(newNeighbor)

        return bfs(node)


if __name__ == '__main__':
    testCases = {
        1: [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ],
        2: [
          ["X"]
        ],
    }

    for key in testCases:
        Solution().solve(testCases[key])
        print(testCases[key])