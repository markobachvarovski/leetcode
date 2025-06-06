from typing import List
from collections import deque


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        charToParentMap = {}

        def getRoot(char):
            if char not in charToParentMap:
                charToParentMap[char] = char
            if charToParentMap[char] != char:
                charToParentMap[char] = getRoot(charToParentMap[char])
            return charToParentMap[char]

        def mergeGroups(char1, char2):
            root1, root2 = getRoot(char1), getRoot(char2)
            if root1 != root2:
                if root1 < root2:
                    charToParentMap[root2] = root1
                else:
                    charToParentMap[root1] = root2

        for i in range(len(s1)):
            mergeGroups(s1[i], s2[i])

        ans = []
        for char in baseStr:
            ans.append(getRoot(char))

        return ''.join(ans)


if __name__ == '__main__':
    testCases = {
        1: ["dccaccbdafgeabeeghbigbhicggfbhiccfgbechdicbhdcgahi",
            "igfcigeciahdafgegfbeddhgbacaeehcdiehiifgbhhehhccde",
            "sanfbzzwblekirguignnfkpzgqjmjmfokrdfuqbgyflpsfpzbo"],
        2: ["parker", "morris", "parser"],
        3: ["hello", "world", "hold"]
    }

    for key in testCases:
        print(Solution().smallestEquivalentString(testCases[key][0], testCases[key][1], testCases[key][2]))
