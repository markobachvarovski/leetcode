
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        minLength = min(len(word1), len(word2))

        for i in range(minLength):
            ans += word1[i] + word2[i]

        if len(word1) == minLength:
            return ans + word2[minLength:]

        return ans + word1[minLength:]


if __name__ == '__main__':
    testCases = {
        1: ["abc", "pqr"],
        2: ["ab", "pqrs"],
        3: ["abcd", "pq"],
        4: ["", "abcd"]
    }

    for key in testCases:
        print(Solution().mergeAlternately(testCases[key][0], testCases[key][1]))