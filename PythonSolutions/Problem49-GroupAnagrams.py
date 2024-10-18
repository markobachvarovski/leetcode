from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        setToList = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            setToList[tuple(count)].append(s)

        return list(setToList.values())


if __name__ == '__main__':
    testCases = {
        1: ["eat","tea","tan","ate","nat","bat"]
    }

    for key in testCases:
        print(f"{Solution().groupAnagrams(testCases[key])}")
