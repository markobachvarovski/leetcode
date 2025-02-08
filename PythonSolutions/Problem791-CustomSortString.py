from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = []

        for c in order:
            ans.append(c * count[c])
            count[c] = 0

        for c in count:
            ans.append(c * count[c])

        return ''.join(ans)


if __name__ == '__main__':
    testCases = {
        1: ['cba', 'abcd'],
        2: ['bcafg', 'bcad']
    }

    for key in testCases:
        print(Solution().customSortString(testCases[key][0], testCases[key][1]))
