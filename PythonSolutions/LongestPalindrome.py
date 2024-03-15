class Solution:
    def longestPalindrome(self, s: str) -> str:
        glbLongestPalindrome = s[0]
        lclLongestPalindrome = s[0]

        for startIndex in range(0, len(s)):
            for stopIndex in range(startIndex, len(s)):
                substring = s[startIndex:stopIndex]
                reverseSubstring = substring[::-1]

                # Scenario 1: Even palindrome with an even or odd stopping index
                if s[startIndex:stopIndex + (stopIndex - startIndex)] == substring + reverseSubstring\
                        or s[startIndex:stopIndex + (stopIndex - startIndex) - 1] == substring + reverseSubstring:
                    lclLongestPalindrome = substring + reverseSubstring
                # Scenario 2: Odd palindrome with even or odd stopping index
                elif s[startIndex:stopIndex + (stopIndex - startIndex)] == substring + reverseSubstring[1:]\
                        or s[startIndex:stopIndex + (stopIndex - startIndex) - 1] == substring + reverseSubstring[1:]:
                    lclLongestPalindrome = substring + reverseSubstring[1:]

                if len(lclLongestPalindrome) > len(glbLongestPalindrome):
                    glbLongestPalindrome = lclLongestPalindrome

        return glbLongestPalindrome

if __name__ == '__main__':
    testStrings = {
        1: "babad",
        2: "cbbd",
        3: "bb",
        4: "abcbe",
        5: "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    }

    for key in testStrings:
        print(
            f"The longest palindromic substring in {testStrings[key]} is: {Solution().longestPalindrome(testStrings[key])}")
