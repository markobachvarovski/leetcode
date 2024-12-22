from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(start_index, path):
            if start_index == len(s):
                ans.append(" ".join(path))
                return
            for end_index in range(start_index, len(s)):
                w = s[start_index:end_index+1]
                if w in wordDict:
                    path.append(w)
                    dfs(end_index+1, path)
                    path.pop()
        ans = []
        dfs(0, [])
        return ans

if __name__ == '__main__':
    testWords = {
        1: ["leetcode", ["leet", "code"]],
        2: ["applepenapple", ["apple","pen"]],
        3: ["catsanddog", ["cat","cats","and","sand","dog"]],
        4: ["cars", ["car","ca","rs"]]
    }

    for key in testWords:
        print(Solution().wordBreak(testWords[key][0], testWords[key][1]))