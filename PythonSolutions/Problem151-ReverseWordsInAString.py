from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        r = len(s) - 1
        l = r - 1

        while l < r and l >= 0:
            while s[r] == " ":
                r -= 1

            l = r

            while s[l] != " ":
                l -= 1

            ans += s[l: r + 1] + " "

            r = l - 1
            l = r - 1

        return ans[:-1]

if __name__ == '__main__':
    testStrings = {
        1: "the sky is blue",
        2: "  hello world  ",
        3: "a good   example"
    }

    for key in testStrings:
        print(Solution().reverseWords(testStrings[key]))
