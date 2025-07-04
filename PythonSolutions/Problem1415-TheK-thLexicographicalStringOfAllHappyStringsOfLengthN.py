
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []

        def dfs(index, comb):
            nonlocal happy_strings
            if index == n:
                happy_strings.append(''.join(comb))
                return
            else:
                for val in ['a', 'b', 'c']:
                    if (len(happy_strings) < k and
                            (len(comb) == 0 or (len(comb) > 0 and comb[-1] != val))):
                        comb.append(val)

                        dfs(index + 1, comb)

                        comb.pop()

        dfs(0, [])
        if len(happy_strings) >= k:
            return happy_strings[k - 1]

        return ''


if __name__ == '__main__':
    testCases = {
        1: [1, 3],
        2: [1, 4],
        3: [3, 9]
    }

    for key in testCases:
        print(Solution().getHappyString(testCases[key][0], testCases[key][1]))