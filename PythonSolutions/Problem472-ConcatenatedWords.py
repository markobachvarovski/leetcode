from typing import List
from collections import Counter

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        freq = Counter(words)
        ans = []

        for word in words:
            dp = [False] * (len(word) + 1)
            dp[0] = True

            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in freq and word[j:i] != word:
                        dp[i] = True
                        break

            if dp[-1]:
                ans.append(word)

        return ans


if __name__ == '__main__':
    testCases = {
        1: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"],
        2: ["cat", "dog", "catdog"]
    }

    for key in testCases:
        print(Solution().findAllConcatenatedWordsInADict(testCases[key]))
