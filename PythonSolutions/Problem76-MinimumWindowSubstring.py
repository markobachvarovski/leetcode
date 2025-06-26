from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        t_count = Counter(t)

        required = len(t_count)
        formed = 0

        minLength = float('inf')
        ans = ""
        curr_count = Counter()

        for right in range(len(s)):
            curr_count[s[right]] += 1

            if s[right] in t_count and curr_count[s[right]] == t_count[s[right]]:
                formed += 1

            while formed == required:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    ans = s[left:right + 1]

                curr_count[s[left]] -= 1
                if s[left] in t_count and curr_count[s[left]] < t_count[s[left]]:
                    formed -= 1
                left += 1

        return ans if minLength != float('inf') else ""

if __name__ == '__main__':
    testCases = {
        1: ["ADOBECODEBANC", "ABC"],
        2: ["b", "b"],
        3: ["a", "aa"]
    }

    for key in testCases:
        print(Solution().minWindow(testCases[key][0], testCases[key][1]))