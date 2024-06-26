from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, wordDict))

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]

if __name__ == '__main__':
    testWords = {
        1: ["leetcode", ["leet", "code"]],
        2: ["applepenapple", ["apple","pen"]],
        3: ["catsandog", ["cats","dog","sand","and","cat"]],
        4: ["cars", ["car","ca","rs"]]
    }

    for key in testWords:
        if Solution().wordBreak(testWords[key][0], testWords[key][1]):
            print(f"{testWords[key][0]} can be broken down in a combination of the following words: {testWords[key][1]}")
        else:
            print(
                f"{testWords[key][0]} can not be broken down in a combination of the following words: {testWords[key][1]}")
