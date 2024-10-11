class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return s[l:r] == s[l:r][::-1] or s[l + 1: r + 1] == s[l + 1: r + 1][::-1]
            else:
                l += 1
                r -= 1

        return True


if __name__ == '__main__':
    testCases = {
        1: "aba",
        2: "abca",
        3: "abc"
    }

    for key in testCases:
        print(Solution().validPalindrome(testCases[key]))