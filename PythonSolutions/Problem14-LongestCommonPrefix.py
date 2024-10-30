from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


if __name__ == '__main__':
    testCases = {
        1: ["flower","flow","flight"],
        2: ["dog","racecar","car"]
    }

    for key in testCases:
        print(Solution().longestCommonPrefix(testCases[key]))
