from typing import List
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        visited = set()
        geneLength = len(startGene)
        letterMutations = ['A', 'C', 'T', 'G']

        q = deque()
        q.append([startGene, 0])
        while q:
            currGene, mutations = q.popleft()

            if currGene == endGene:
                return mutations

            visited.add(currGene)

            for i in range(geneLength):
                for letter in letterMutations:
                    tempGene = list(currGene)
                    tempGene[i] = letter
                    tempGene = "".join(tempGene)

                    if tempGene in bankSet and tempGene not in visited:
                        q.append([tempGene, mutations + 1])

        return -1

if __name__ == '__main__':
    testCases = {
        1: [
            "AACCGGTT",
            "AACCGGTA",
            ["AACCGGTA"]
        ],
        2: [
            "AACCGGTT",
            "AAACGGTA",
            ["AACCGGTA","AACCGCTA","AAACGGTA"]
        ]
    }

    for key in testCases:
        print(Solution().minMutation(testCases[key][0], testCases[key][1], testCases[key][2]))