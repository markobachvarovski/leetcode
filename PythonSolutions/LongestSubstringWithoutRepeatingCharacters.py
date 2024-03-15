class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChars = {}
        glbMaxLength = 0
        lclMaxLength = 0
        i = 0
        while i < len(s):
            if s[i] not in seenChars:
                seenChars[s[i]] = 1
                lclMaxLength += 1
            else:
                i -= lclMaxLength
                lclMaxLength = 0
                seenChars = {}

            if lclMaxLength > glbMaxLength:
                glbMaxLength = lclMaxLength
            i += 1

        return glbMaxLength

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

