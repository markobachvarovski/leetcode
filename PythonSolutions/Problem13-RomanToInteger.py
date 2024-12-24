class Solution:
    def romanToInt(self, s: str) -> int:
        symbolToValue = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i, char in enumerate(s):
            total += symbolToValue[char]

            if  i - 1 >= 0 and symbolToValue[s[i - 1]] < symbolToValue[char]:
                total -= symbolToValue[s[i - 1]] * 2

        return total


if __name__ == '__main__':
    testCases = {
        1: "MMMCDXC"
    }

    for key in testCases:
        print(Solution().romanToInt(testCases[key]))
