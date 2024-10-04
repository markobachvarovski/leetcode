class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(l, r):
            nonlocal totalPalindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                totalPalindromes += 1
                l -= 1
                r += 1

        totalPalindromes = 0
        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)

        return totalPalindromes


if __name__ == '__main__':
    testStrings = {
        1: "abc",
        2: "aaa",
    }

    for key in testStrings:
        print(Solution().countSubstrings(testStrings[key]))
