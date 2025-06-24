class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeats = (len(b) + len(a) - 1) // len(a)

        if b in a * min_repeats:
            return min_repeats

        if b in a * (min_repeats + 1):
            return min_repeats + 1

        return -1



if __name__ == '__main__':
    testCases = {
        1: ["abcd", "cdabcdab"],
        2: ["a", "aa"]
    }

    for key in testCases:
        print(Solution().repeatedStringMatch(testCases[key][0], testCases[key][1]))