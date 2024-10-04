from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countDict = {}
        l, r = 0, 0
        countOfMostFrequentLetter = 0

        for r in range(len(s)):
            countDict[s[r]] = 1 + countDict.get(s[r], 0)
            countOfMostFrequentLetter = max(countOfMostFrequentLetter, countDict[s[r]])

            if (r - l + 1) - countOfMostFrequentLetter > k:
                countDict[s[l]] -= 1
                l += 1

        return r - l + 1

if __name__ == '__main__':
    testCases = {
        1: ["XYYX", 2],
        2: ["AAABABB", 1],
        3: ["AABABBA", 1]
    }

    for key in testCases:
        print(Solution().characterReplacement(testCases[key][0], testCases[key][1]))

