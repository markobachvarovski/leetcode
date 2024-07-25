class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        l = 0

        for r in range(n):
            if s[r] not in charSet:
                charSet.add(s[r])
                maxLength = max(maxLength, r - l + 1)
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])

        return maxLength

if __name__ == '__main__':
    testStrings = {
        1: "abcabcbb",
        2: "bbbbb",
        3: "pwwkew",
        4: " ",
        5: "aab"
    }

    for key in testStrings:
        print(f"The longest substring in {testStrings[key]} is: {Solution().lengthOfLongestSubstring(testStrings[key])}")

